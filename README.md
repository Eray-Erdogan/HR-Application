markdown
Kodu kopyala
# HR Q&A with Eray

## Description
HR Q&A with Eray is an interactive application that allows users to ask questions about HR policies using natural language processing. The application utilizes LangChain for text processing and AWS Bedrock for language modeling, providing an efficient and responsive interface for HR-related inquiries.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. **Prerequisites**: Ensure you have Python installed (version 3.7 or higher).
2. **Clone the repository**:
   ```bash
   git clone https://github.com/Eray-Erdogan/HR-Application.git
   cd HR-Application
Install the required libraries:
bash
Kodu kopyala
pip install langchain langchain-community streamlit
Set up AWS credentials to access Bedrock services.
Usage
Run the Streamlit application:

bash
Kodu kopyala
streamlit run app.py
Open your web browser and go to http://localhost:8501 to start interacting with the HR Q&A interface.

Example Usage:

Enter your HR-related questions in the text area and click the "Learn GenAI with Bayram Eray Erdoğan" button to get responses.
Code Structure
app.py: The main Streamlit application that serves the user interface.
App_backend.py: Contains the backend logic, including loading the PDF, processing text, creating embeddings, and handling queries.
requirements.txt: Lists the project dependencies.
Key Functions
hr_index(): Loads the HR policy PDF, splits the text into manageable chunks, and creates a vector index for embedding.
hr_llm(): Connects to the Bedrock Foundation Model to process natural language queries.
hr_rag_response(index, question): Searches the vector index for the best match based on the user’s question and retrieves the response from the language model.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes.
Push your branch and submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Eray Erdoğan - eray.erdogan@ozu.edu.tr
