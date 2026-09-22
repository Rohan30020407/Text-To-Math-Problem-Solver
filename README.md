# 🧮 Text To Math Problem Solver

A Streamlit-based AI math problem solver powered by **Groq** and **LLaMA**. The application calculates mathematical problems and provides clear step-by-step explanations.

## 🚀 Features

* Solve mathematical expressions using AI
* Step-by-step explanations
* Supports arithmetic and word problems
* Groq API integration
* Interactive Streamlit interface
* Chat history using Streamlit Session State
* Error handling for invalid requests

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq
* LLaMA
* PromptTemplate

## 📂 Project Structure

```text
Text-To-Math-Problem-Solver/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── main-interface.png
    ├── math-problem.png
    ├── solution.png
    └── example.png
⚙️ Installation

Clone the repository:

git clone <YOUR_REPOSITORY_URL>
cd Text-To-Math-Problem-Solver
Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

The application will open at:

http://localhost:8501

🔑 Groq API Key

Enter your Groq API key in the Streamlit sidebar when the application starts.

Do not upload your API key to GitHub.

💡 Example
Input
100 + 800 - 950
Output
Result: -50

The application also provides a step-by-step explanation of the calculation.

📸 Application Screenshots
Main Interface

Math Problem

Generated Solution

Example

👨‍💻 Author

Rohan Soni