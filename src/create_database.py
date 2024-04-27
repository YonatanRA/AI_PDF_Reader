from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader

from tools import logger
import os                          
from dotenv import load_dotenv 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_db() -> None:

    """
    Function to create ChromaDB
    """

    global OPENAI_API_KEY

    logger.info('Loading and Chunking PDF file.')
    loader = PyPDFDirectoryLoader("../pdfs/")
    chunks = loader.load_and_split()

    logger.info('Loading embedding model.')
    vectorizer = OpenAIEmbeddings()

    logger.info('Storing embeddings in ChromaDB.')
    Chroma.from_documents(chunks, 
                          vectorizer, 
                          persist_directory="../chroma_db")
    logger.info('Done.')
    

if __name__=='__main__':
    create_db()