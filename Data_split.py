# 1.	Import the necessary libraries: OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, and Bedrock-LLM.

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 2.	Define the data source and load the data using the PDF Loader from the following link: Leave Policy PDF.
# 3.	Split the text based on characters and tokens:
data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=10, chunk_overlap=1)
data= "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for  will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
print(data_split.split_text(data))


#     •	Recursively split by character: ["\n\n", "\n"].
# 4.	Establish a connection to the Embeddings Client.
# 5.	Create a Vector DB, store the embeddings, and index them for search purposes:
# 6.	Write a function to connect to the Bedrock Foundation Model:
#     •	Name the function VectorstoreIndexCreator.
# 7.	Write a function that searches the user prompt, finds the best match from the Vector DB, and sends both to the Bedrock-LLM.

