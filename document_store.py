#delete index cmd: curl -XDELETE localhost:9200/document

from haystack.document_stores import ElasticsearchDocumentStore
document_store = ElasticsearchDocumentStore(host="host_address", port="port_address",
scheme="https", username="", password="", index="documents")

from haystack.nodes import PreProcessor
from haystack.utils import convert_files_to_dicts 

doc_dir_lists = ['Wiki_Data/fmt_txt/001','Wiki_Data/fmt_txt/002','Wiki_Data/fmt_txt/003', 
                    'Wiki_Data/fmt_txt/004','Wiki_Data/fmt_txt/005','Wiki_Data/fmt_txt/006',
                    'Wiki_Data/fmt_txt/007','Wiki_Data/fmt_txt/008','Wiki_Data/fmt_txt/009',
                    'Wiki_Data/fmt_txt/010','Wiki_Data/fmt_txt/011','Wiki_Data/fmt_txt/012']

def push_DataToElastic(doc_dir):
    alldocs=[]
    # Convert files to dicts
    alldocs = convert_files_to_dicts(dir_path=doc_dir, split_paragraphs=True)
    # Preprocess Define
    processor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=True,
        split_by="word",
        split_length=300,
        split_respect_sentence_boundary=True,
        split_overlap=0
    )
    print("Uploading...")
    # Preprocess + Split => Paragraph => can be used for optimize for retriver and reader
    # preprocess all content in all docs dictionary (paragraph will be split into a list)
    docs= [processor.process(contents) for contents in alldocs] 
    # load paragraphs (of one doc in docs) to an individual content in dictionary (formating)
    dicts= [paragraph for doc in docs for paragraph in doc] 
    document_store.write_documents(dicts)
    # Wait for ~2 mininutes
    # Load dictionay to document_store
    print ("Done")

for doc_dir in doc_dir_lists:
    print(doc_dir)
    push_DataToElastic(doc_dir)
