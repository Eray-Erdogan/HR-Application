# 1.	Import the necessary libraries: OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, and Bedrock-LLM.

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms.bedrock import Bedrock
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
from langchain.indexes import vectorstore, VectorstoreIndexCreator

def hr_index():
    # 2.	Define the data source and load the data using the PDF Loader from the following link: Leave Policy PDF.
    data_load = PyPDFLoader('https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=20379&mevzuatTur=KurumVeKurulusYonetmeligi&mevzuatTertip=5')

    # 3.	Split the text based on characters and tokens    •	Recursively split by character: ["\n\n", "\n"].
    data_split = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=100, chunk_overlap=10)

    # 4.	Establish a connection to the Embeddings Client.
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name='default',
        model_id="amazon.titan-embed-text-v1")

    # 5.	Create a Vector DB, store the embeddings, and index them for search purposes:
    data_index = VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS)

    # 5.b Create index for HR Policy Document
    db_index = data_index.from_loaders([data_load])
    return db_index

# 6.	Write a function to connect to the Bedrock Foundation Model:
#     •	Name the function VectorstoreIndexCreator.
def hr_llm():
    llm=Bedrock(
        credentials_profile_name='default',
        model_id='anthropic.claude-v2',
        model_kwargs={
            "max_tokens_to_sample": 3000,
            "temperature": 0.1,
            "top_p": 0.9})
    return llm

# 7.	Write a function that searches the user prompt, finds the best match from the Vector DB, and sends both to the Bedrock-LLM.

def hr_rag_response(index,question):
    rag_llm=hr_llm()
    hr_rag_query=index.query(question=question,llm=rag_llm)
    return hr_rag_query



