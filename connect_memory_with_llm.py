"""
This script connects the pre-built FAISS vector store with the LLM to create a question-answering system.

It performs the following steps:
1. Loads the FAISS vector store from the local filesystem.
2. Loads the embedding model and the large language model (LLM).
3. Sets up a custom prompt template for the QA chain.
4. Creates a RetrievalQA chain to answer questions based on the knowledge base.
5. Enters an interactive loop to accept user queries and provide answers.
"""

import os
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from Resources import load_embedding_model, load_llm
import config

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

def set_custom_prompt() -> PromptTemplate:
    """
    Creates and returns a custom prompt template for the QA chain.

    Returns:
        PromptTemplate: The custom prompt template.
    """
    return PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"]
    )

def create_qa_chain():
    """
    Creates and returns the RetrievalQA chain.

    Returns:
        RetrievalQA: The question-answering chain.
    """
    # Load the FAISS vector store
    print("📚 Loading comprehensive finance knowledge base...")
    embedding_model = load_embedding_model()
    db = FAISS.load_local(
        config.DB_FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True,
    )
    print("✅ Knowledge base loaded successfully!")

    # Create the QA chain
    return RetrievalQA.from_chain_type(
        llm=load_llm(),
        chain_type="stuff",
        retriever=db.as_retriever(
            search_type="similarity", search_kwargs={"k": 4}
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt": set_custom_prompt()},
    )

def main():
    """
    Main function to run the finance AI assistant.
    """

    # Create the QA chain
    qa_chain = create_qa_chain()

    # Interactive loop
    print("\n🤖 Finance AI Assistant is ready!")
    print("💡 Ask about budgeting, investing, debt management, retirement, or taxes.")
    print("-" * 60)

    user_query = input("Ask your personal finance question: ")

    if user_query.strip():
        response = qa_chain.invoke({"query": user_query})
        print("\nFinance Assistant Response:", response["result"].strip())
        print("-" * 60)

if __name__ == "__main__":
    main()
