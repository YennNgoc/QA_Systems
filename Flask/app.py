# import packages
import json
import os
import logging
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
#from haystack import Finder
from haystack.reader.farm import FARMReader
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever
from haystack.pipelines import ExtractiveQAPipeline

#application settings
app = Flask(__name__)
CORS(app)
#initialization of the Haystack Elasticsearch document storage
document_store = ElasticsearchDocumentStore(host="qa-system.es.us-central1.gcp.cloud.es.io", port="9243",
scheme="https", username="elastic", password="6e7MQjacsRjCDKI2lKHsWVzv", index="documents")
print('Document Store ready...!')
# initialization of ElasticRetriever
retriever = ElasticsearchRetriever(document_store= document_store)
print('Retriever ready...!')
# Reader model
reader = FARMReader(model_name_or_path="my_model/", use_gpu=True)
print('Reader ready...!')

@app.route('/')
def home():
    """Return a friendly HTTP greeting."""
    return 'Hello QNA API is running'

@app.route('/qna', methods=['GET','POST'])
def qna():
    answ=None
    if request.method == "POST": 
        """Return the n answers."""
        question = request.form['question']
        # index is the target document where queries need to sent.
        #index = request.form['index']
       
        
        
        # Pipeline to answer questions.
        #pipe = ExtractiveQAPipeline(reader, retriever)
        #print('Pipe ready...!')

        candidate_documents = retriever.retrieve(
        query=question, top_k=10,)
        #prediction=candidate_documents[0]
        '''
        for doc in candidate_documents:
            print(doc)
        
        prediction = pipe.run(
        #query="Một trong những nữ diễn viên kịch nói đầu tiên ở Việt Nam?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
        #query="huyện Quỳnh Phụ thuộc tỉnh nào?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
        #query="trụ cột của nền kinh tế Qatar là gì?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
        #query="Voldemort là ai", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
        query= question, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}}
        )'''
        print("Reader running...")
        result = reader.predict(
            query=question,
            documents=candidate_documents,
            top_k=3)
        print("Query running...")
        # Document <-> Retriever
        # Answer from Document <-> Reader
        answ=  result["answers"][0].answer
        
    else:
        question = ""
        answ = ""

    #test on cmd
    #print(question)
    #print(answ)

    return render_template("index.html",question=question, ans= answ) #jsonify([doc.to_json() for doc in candidate_documents])


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return json.dumps({'status':'failed','message':
        """An internal error occurred: <pre>{}</pre>See logs for full stacktrace.""".format(e),
                       'result': []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8777)
