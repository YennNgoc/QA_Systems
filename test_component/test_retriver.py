from haystack.document_stores import ElasticsearchDocumentStore
document_store = ElasticsearchDocumentStore(host="localhost",port="9200", username="", password="", index="document")

# Load Retriever
from haystack.nodes import ElasticsearchRetriever
retriever = ElasticsearchRetriever(document_store = document_store)

question = "Phạm Văn Đồng giữ chức vụ gì trong bộ máy Nhà nước Cộng hòa Xã hội chủ nghĩa Việt Nam?"
candidate_documents = retriever.retrieve(
    query=question
)
print(candidate_documents)