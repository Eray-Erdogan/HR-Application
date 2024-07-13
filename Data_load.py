# 1.	Import the necessary libraries: OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, and Bedrock-LLM.

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 2.	Define the data source and load the data using the PDF Loader from the following link: Leave Policy PDF.
data_load=PyPDFLoader('https://isc2rduchapter.org/wp-content/uploads/2019/02/CISSP.pdf')
data_test=data_load.load_and_split()
print(len(data_test))
print(data_test[66])


# 3.	Split the text based on characters and tokens:
#     •	Recursively split by character: ["\n\n", "\n"].
# 4.	Establish a connection to the Embeddings Client.
# 5.	Create a Vector DB, store the embeddings, and index them for search purposes:
# 6.	Write a function to connect to the Bedrock Foundation Model:
#     •	Name the function VectorstoreIndexCreator.
# 7.	Write a function that searches the user prompt, finds the best match from the Vector DB, and sends both to the Bedrock-LLM.
