# /home/ravi/Projects/pankaj/FinanceGPT/config.py
"""
Configuration settings for the FinanceGPT application.

This file centralizes all the configuration variables for the project,
making it easier to manage and modify settings.
"""

# --- LLM Configuration ---
# Repository ID for the large language model on Hugging Face Hub.
# The current model is chosen for its instruction-following capabilities.
LLM_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"

# Parameters for the Hugging Face text generation endpoint.
LLM_ENDPOINT_PARAMS = {
    "task": "text-generation",
    "max_new_tokens": 512,
    "do_sample": False,
    "repetition_penalty": 1.03,
    "provider": "auto",
}

# --- Embedding Model Configuration ---
# Model name for sentence-transformers. Used for creating vector embeddings.
# 'all-MiniLM-l6-v2' is a good starting point for performance and quality.
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-l6-v2"

# Keyword arguments for the embedding model.
# Using 'cpu' is recommended if a GPU is not available.
EMBEDDING_MODEL_KWARGS = {'device': 'cpu'}

# Keyword arguments for encoding text.
# 'normalize_embeddings' is set to False by default.
EMBEDDING_ENCODE_KWARGS = {'normalize_embeddings': False}

# --- Vector Store Configuration ---
# Path to the local FAISS vector store database.
DB_FAISS_PATH = "vectorstore/db_faiss"

# Path to the directory containing the source documents for the knowledge base.
DATA_PATH = "data/"

# --- Text Splitting Configuration ---
# Parameters for splitting documents into chunks.
TEXT_SPLITTER_PARAMS = {
    "chunk_size": 2000,
    "chunk_overlap": 400,
}