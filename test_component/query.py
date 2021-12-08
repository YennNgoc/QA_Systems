import requests
import json
import pprint
# connect Elastic server and test some query
headers = {'content-type': 'application/json','charset':'utf-8'}
uri="http://127.0.0.1:9200/document/_search"
def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "content": term
            }
        }
    })
    response = requests.get(uri, data=query,headers=headers)
    results = json.loads(response.text)
    return results
res=search(uri, "Đại học khoa học tự nhiên")

# iterate the nested dictionaries inside the ["hits"]["hits"] list
for num, doc in enumerate(res['hits']['hits']):
    print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")
   
    # Use 'iteritems()` instead of 'items()' if using Python 2
    for key, value in doc.items():
        print (key, "-->", value)
   
    # print a few spaces between each doc for readability
    print ("\n\n")
#pprint.pprint(res['hits']['hits'])


