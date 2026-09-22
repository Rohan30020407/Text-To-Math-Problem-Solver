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
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd Text-To-Math-Problem-Solver
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

## 🔑 Groq API Key

Enter your Groq API key in the Streamlit sidebar when the application starts.

**Do not upload your API key to GitHub.**

## 💡 Example

### Input

```text
100 + 800 - 950
```

### Output

```text
Result: -50
```

The application also provides a step-by-step explanation of the calculation.

## 📸 Application Screenshots

Add screenshots of the application inside the `screenshots` folder and reference them here.

## 👨‍💻 Author

Rohan Soni
