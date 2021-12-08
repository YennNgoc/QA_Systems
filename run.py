from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import ElasticsearchRetriever
from haystack.nodes import FARMReader#, TransformersReader
from haystack.pipelines import ExtractiveQAPipeline

document_store = ElasticsearchDocumentStore(host="localhost",port="9200", username="", password="", index="document")

# Load Retriever
retriever = ElasticsearchRetriever(document_store = document_store)
print("Retriever done")
# Load Reader
# Load a  local model or any of the QA models on
# Hugging Face's model hub (https://huggingface.co/models)
#from haystack.utils import clean_wiki_text, convert_files_to_dicts, fetch_archive_from_http, print_answers


reader = FARMReader(model_name_or_path="Flask/my_model")
print("Reader done")
# Create Pipelines

pipe = ExtractiveQAPipeline(reader, retriever)

# Query to predict  (tui thấy answer top dưới đúng hơn top 1)
prediction = pipe.run(
    #query="Một trong những nữ diễn viên kịch nói đầu tiên ở Việt Nam?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
    #query="huyện Quỳnh Phụ thuộc tỉnh nào?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
    #query="trụ cột của nền kinh tế Qatar là gì?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
    #query="Voldemort là ai", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
    query="Dercetina discoidalis là gì?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)
print("Query running...")
# Document <-> Retriever
# Answer from Document <-> Reader
print(prediction)