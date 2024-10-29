HR Q&A with Eray
Welcome to the HR Q&A with Eray project! This project utilizes LangChain and AWS Bedrock to create a question-and-answer interface based on HR policies extracted from a PDF document.

Table of Contents
Overview
Installation
Usage
Code Structure
Contributing
License
Overview
This project allows users to interactively ask questions about HR policies. The core functionality is built using LangChain for text processing and embeddings, AWS Bedrock for language modeling, and Streamlit for the user interface.

Installation
To get started, ensure you have Python installed, and then install the necessary libraries using pip:

bash
Kodu kopyala
pip install langchain langchain-community streamlit
You'll also need to set up AWS credentials for accessing Bedrock services.

Usage
Clone the repository:

bash
Kodu kopyala
git clone https://github.com/yourusername/hr-qa-eray.git
cd hr-qa-eray
Run the Streamlit app:

bash
Kodu kopyala
streamlit run app.py
Open your web browser and go to http://localhost:8501 to interact with the HR Q&A interface.

Code Structure
app.py: The main Streamlit application for the user interface.
App_backend.py: Contains the backend logic, including PDF loading, text splitting, embedding, and querying.
requirements.txt: Lists the dependencies required for the project.
Key Functions
hr_index(): Loads the HR policy PDF, splits the text, and creates a vector index for embedding.
hr_llm(): Establishes a connection to the Bedrock Foundation Model.
hr_rag_response(index, question): Processes user queries against the vector index and returns the response from the Bedrock model.
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes.
Push your branch and create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
