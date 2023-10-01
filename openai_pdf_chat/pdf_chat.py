from dotenv import load_dotenv #to load open Ai API key
from langchain.embeddings.openai import OpenAIEmbeddings # to convert text to embeddings
from langchain.vectorstores import FAISS  # to convert text to embeddings
import pickle  # to save embeddings
import os #  to deal with file path
from langchain.chat_models import ChatOpenAI  # to deal with chat GPT
from langchain.chains.question_answering import load_qa_chain  # to deal with chat GPT
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from bidi.algorithm import get_display


def main(incoming_msg):
    # load_dotenv() 
                        
    loader = DirectoryLoader('../data_', glob="**/*.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

      # True --> we worked this file befor 
    with open("../data_/data.pkl", "rb") as f:
        db = pickle.load(f)


    # incoming_msg = incoming_msg.strip()
    if incoming_msg:
        # print(get_display(incoming_msg))
        print("****",incoming_msg, "****")
        # print("****",type(incoming_msg), "****")
        docs = db.similarity_search(query=incoming_msg, k=1)
        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        chain = load_qa_chain(llm=llm, chain_type="stuff") 
        response = chain.run(question=incoming_msg,input_documents=docs)
        return response
