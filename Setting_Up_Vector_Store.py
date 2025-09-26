# /home/ravi/Projects/pankaj/FinanceGPT/Setting_Up_Vector_Store.py
"""
This script builds and saves a FAISS vector store from documents in the data directory.

It performs the following steps:
1. Loads documents from the specified data directory.
2. Splits the documents into optimized text chunks.
3. Creates vector embeddings for the chunks using a sentence-transformer model.
4. Saves the resulting FAISS vector store to the local filesystem.

The script is designed to be run as a standalone process to set up the knowledge base
for the FinanceGPT application.
"""

from typing import List

from langchain.docstore.document import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    DirectoryLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

import config
from Resources import load_embedding_model

def load_documents(data_path: str) -> List[Document]:
    """
    Loads all supported documents (PDF and TXT) from the specified directory.

    Args:
        data_path (str): The path to the directory containing the documents.

    Returns:
        List[Document]: A list of loaded documents.
    """
    print(f"Loading documents from: {data_path}")
    documents = []

    # Load PDF files
    try:
        pdf_loader = DirectoryLoader(
            data_path, glob="*.pdf", loader_cls=PyPDFLoader, show_progress=True
        )
        pdf_docs = pdf_loader.load()
        documents.extend(pdf_docs)
        print(f"Successfully loaded {len(pdf_docs)} PDF pages.")
    except Exception as e:
        print(f"Could not load PDFs: {e}")

    # Load text files
    try:
        txt_loader = DirectoryLoader(
            data_path, glob="*.txt", loader_cls=TextLoader, show_progress=True
        )
        txt_docs = txt_loader.load()
        documents.extend(txt_docs)
        print(f"Successfully loaded {len(txt_docs)} text documents.")
    except Exception as e:
        print(f"Could not load text files: {e}")

    print(f"Total documents loaded: {len(documents)}")
    return documents


def create_text_chunks(docs: List[Document]) -> List[Document]:
    """
    Splits the loaded documents into smaller text chunks.

    Args:
        docs (List[Document]): The list of documents to split.

    Returns:
        List[Document]: A list of text chunks.
    """
    print("Splitting documents into text chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        **config.TEXT_SPLITTER_PARAMS,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = text_splitter.split_documents(docs)
    print(f"Created {len(chunks)} text chunks.")
    return chunks


def build_and_save_vector_store(chunks: List[Document]):
    """
    Builds a FAISS vector store from the text chunks and saves it locally.

    Args:
        chunks (List[Document]): The list of text chunks to embed.
    """
    print("Loading embedding model...")
    embedding_model = load_embedding_model()

    print("Creating embeddings and building FAISS vector store...")
    db = FAISS.from_documents(chunks, embedding_model)

    print(f"Saving vector store to: {config.DB_FAISS_PATH}")
    db.save_local(config.DB_FAISS_PATH)
    print("Vector store saved successfully.")

def main():
    """
    Main function to run the vector store setup process.
    """
    print("--- Starting Knowledge Base Setup ---")

    # Step 1: Load documents
    documents = load_documents(config.DATA_PATH)

    if not documents:
        print("No documents were loaded. Aborting setup.")
        return

    # Step 2: Create text chunks
    text_chunks = create_text_chunks(documents)

    # Step 3: Build and save the vector store
    build_and_save_vector_store(text_chunks)

    print("--- Knowledge Base Setup Complete ---")
    print("\n🎉 Comprehensive finance knowledge base created successfully!")
    print(f"Total chunks embedded: {len(text_chunks)}")
    print(f"Vector store saved at: {config.DB_FAISS_PATH}")


if __name__ == "__main__":
    main()
