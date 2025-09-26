# /home/ravi/Projects/pankaj/FinanceGPT/financebot_no_auth.py
"""
This script runs the FinanceGPT Streamlit application without authentication.

It provides a web interface for the finance AI assistant, including
chat functionality, and financial calculators.
"""

import os
import streamlit as st
import warnings
from dotenv import load_dotenv, find_dotenv

from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

from finance_calculators import render_financial_calculators
from Resources import load_embedding_model, load_llm
import config

# --- Load Environment Variables ---
load_dotenv(find_dotenv())

# --- Suppress Warnings ---
warnings.filterwarnings("ignore", category=FutureWarning)

# --- Custom Prompt Template ---
CUSTOM_PROMPT_TEMPLATE = """
You are a knowledgeable personal finance assistant. Use the pieces of information provided in the context to answer the user's financial question.

Focus on providing practical, actionable advice about:
- Budgeting and saving strategies
- Investment planning and portfolio management
- Debt management and credit improvement
- Retirement planning and goal setting
- Tax planning and optimization
- Insurance and risk management

If you don't know the answer based on the provided context, just say that you don't know; don't make up financial advice.
Always remind users to consult with qualified financial professionals for personalized advice.
Stick strictly to the given context and avoid speculation.

Context: {context}
Question: {question}

Provide helpful, accurate financial guidance based on the context above.
"""

@st.cache_resource
def create_qa_chain():
    """
    Creates and returns the RetrievalQA chain.

    This function is cached to avoid reloading the models on every interaction.

    Returns:
        RetrievalQA: The question-answering chain.
    """
    # Load the FAISS vector store
    embedding_model = load_embedding_model()
    db = FAISS.load_local(
        config.DB_FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True,
    )

    # Create a prompt template
    prompt = PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"]
    )

    # Create the QA chain
    return RetrievalQA.from_chain_type(
        llm=load_llm(),
        chain_type="stuff",
        retriever=db.as_retriever(
            search_type="similarity", search_kwargs={"k": 4}
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )

def main():
    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(page_title="FinanceGPT", page_icon="💰")
    st.title("💰 AI Personal Finance Assistant")

    # --- Session State Initialization ---
    if "show_calculators" not in st.session_state:
        st.session_state.show_calculators = False
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # --- Sidebar ---
    with st.sidebar:
        st.title("💰 Finance Assistant Settings")
        st.info("💡 Ask me about budgeting, investing, saving, debt management, and financial planning!")

        st.divider()
        if st.button("🧮 Financial Calculators", use_container_width=True):
            st.session_state.show_calculators = True
        if st.button("💬 Finance Chat", use_container_width=True):
            st.session_state.show_calculators = False

    # --- Main Content ---
    if st.session_state.show_calculators:
        render_financial_calculators()
    else:
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("Ask your financial question"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        qa_chain = create_qa_chain()
                        response = qa_chain.invoke({"query": prompt})
                        result = response["result"]
                        st.markdown(result)
                        st.session_state.messages.append({"role": "assistant", "content": result})
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
