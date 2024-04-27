# libraries   
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI   
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import argparse
from tools import logger
import os                          
from dotenv import load_dotenv   



# load API KEY
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# query argparsing
argparser = argparse.ArgumentParser(description="PDF Reader query")
argparser.add_argument("-q", "--query", type=str, help="User query input")
parse_args = argparser.parse_args()
query = parse_args.query



def create_prompt() -> object:

    """
    Function to create prompt template.

    Params: No input parameters.

    Return: LangChain ChatPromptTemplate object.
    """

    template = """
            Answer the question based on the context below. If you can't 
            answer the question, reply "I don't know".

            Context: {context}

            Question: {question}
            """
    
    prompt = ChatPromptTemplate.from_template(template)

    return prompt




def get_response() -> str:

    """
    Function to create chatbot response.

    Params: No input parameters.

    Return: string response.
    """

    global OPENAI_API_KEY, query

    logger.info("Creating prompt template.")
    prompt = create_prompt()
    logger.info("Prompt template created.")

    logger.info("Loading GPT and Embedding model.")
    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4-turbo")
    vectorizer = OpenAIEmbeddings()

    logger.info("Getting relevant documents from ChromaDB.")
    chroma_db = Chroma(persist_directory="../chroma_db", embedding_function=vectorizer)
    retriever = chroma_db.as_retriever(search_type="mmr", search_kwargs={"k": 15, "lambda_mult": 0.25})

    parser = StrOutputParser()
    
    logger.info("Executing chain.")
    chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | model | parser

    return chain.invoke(query)


if __name__=='__main__':
    logger.info(f"Chat Response: {get_response()}")