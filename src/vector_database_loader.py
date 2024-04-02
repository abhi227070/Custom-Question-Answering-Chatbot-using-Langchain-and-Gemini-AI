from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader


file_location = "vector_database_file"
data_location = "Custom Question-Answering Chatbot using Google Gemini and Langchain\data\question-answer.csv"

def vector_database():
    
    loader = CSVLoader(file_path=data_location,source_column="prompt",encoding='cp1252')
    data = loader.load()
    embeddings = HuggingFaceInstructEmbeddings()
    vectordb = FAISS.from_documents(documents = data, embedding = embeddings)
    vectordb.save_local(file_location)
    
    return embeddings

def get_embedding():
    embeddings = HuggingFaceInstructEmbeddings()
    return embeddings
    
if __name__ == "__main__":
    vector_database()