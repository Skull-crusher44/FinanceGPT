# /home/ravi/Projects/pankaj/FinanceGPT/Resources.py
"""
This module provides functions to load the AI/ML models required for the FinanceGPT application.

It handles the loading of the embedding model and the large language model (LLM)
using configurations from the central `config.py` file.
"""

import os
from dotenv import load_dotenv
from langchain_huggingface import (
    HuggingFaceEmbeddings,
    HuggingFaceEndpoint,
    ChatHuggingFace,
)
from langchain.embeddings.base import Embeddings
from langchain.llms.base import LLM

import config

# Load environment variables from .env file
load_dotenv(override=True)

def load_embedding_model() -> Embeddings:
    """
    Loads the sentence-transformer model for creating text embeddings.

    The model configuration is sourced from the `config.py` file.

    Returns:
        Embeddings: An instance of the HuggingFaceEmbeddings class.
    """
    return HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs=config.EMBEDDING_MODEL_KWARGS,
        encode_kwargs=config.EMBEDDING_ENCODE_KWARGS,
    )

def load_llm() -> LLM:
    """
    Loads the large language model (LLM) from the Hugging Face Hub.

    The model repository ID and endpoint parameters are sourced from `config.py`.
    Requires an HF_TOKEN environment variable for authentication.

    Returns:
        LLM: An instance of the ChatHuggingFace class.
    """
    # Ensure the Hugging Face token is available
    if "HF_TOKEN" not in os.environ:
        raise ValueError("HF_TOKEN environment variable not set.")

    # Set up the LLM endpoint
    llm_endpoint = HuggingFaceEndpoint(
        repo_id=config.LLM_REPO_ID, **config.LLM_ENDPOINT_PARAMS
    )

    # Wrap the endpoint in a chat model interface
    return ChatHuggingFace(llm=llm_endpoint)
