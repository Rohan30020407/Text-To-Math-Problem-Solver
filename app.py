import streamlit as st
from langchain_groq import ChatGroq
# from langchain.chains import LLMChain ,LLMMathChain
from langchain.chains import LLMChain ,LLMMathChain
from langchain.prompts import PromptTemplate

# --------------------------------
# Streamlit UI Configuration
# --------------------------------
st.set_page_config(
    page_title="Text To Math Problem Solver",
    page_icon="🧮",
    layout="centered"
)

st.title(" 🧮 Text To Math Problem Solver")
st.caption("Powered by Groq  (LLaMA 3.1)")

# ----------------------------------
# API Key Input
# ----------------------------------
groq_api_key = st.sidebar.text_input(
    "Enter your Groq API Key" ,
    type="password"
)

if not groq_api_key:
    st.info("Please add your Groq API key to continue.")
    st.stop()

# -----------------------------------
# Initialize LLM
# -----------------------------------
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=groq_api_key
)

# -----------------------------------
# Math Chain (for calculation)
# -----------------------------------
# math_chain = LLMMathChain.from_llm(
#     llm=llm,
#     verbose=False
# )

# -----------------------------------
# Explaination Chain
# -----------------------------------
explanation_prompt = """
Solve the following math problem step by step.
Explain the reasoning clearly in points and end with final numeric answer.

Question: {question}

Answer:
"""

prompt_template = PromptTemplate(
    input_variables={"question"},
    template=explanation_prompt
)

explanation_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# ------------------------------------
# Session State  (Chat History)
# ------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi  👋 I am a math solver. Enter any math problem and i will solve it step by step. "
        }
    ]

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message (msg["role"]) .write (msg["content"])

# -----------------------------------
# User Input
# ----------------------------------
question = st.text_area(
    "Enter your math problem:",
    # value="100 + 800 -950",
    height=120
)
# ------------------------------------
# Solve Button
# ------------------------------------
if st.button("Find My Answer"):
    if not question.strip():
        st.warning("Please enter a math problem.")
    else:
        # Show user message
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.chat_message("user").write(question)

        try:
            with st.spinner("Solving..."):
                #  Calculate numeric result
             math_result = llm.invoke(
            f"Calculate this math problem and return ONLY the final numeric answer: {question}"
            ).content

            #  General explanation
            explanation = explanation_chain.run(
                    question=question
                )

            final_response = f"""
### ✅  Final Answer
**Result:**  `{math_result}`

---

###  🧠 Step-by-step Explanation
{explanation}
"""
            #  Store and display assistant response
            st.session_state.messages.append(
                {"role":  "assistant", "content":  final_response}
            )
            st.chat_message("assistant").write (final_response)

        except Exception as e:
            st.error(f"Something went wrong:  {e}")
