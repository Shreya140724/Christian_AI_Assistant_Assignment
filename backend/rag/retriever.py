import os
import re
import json

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


VECTOR_STORE_PATH = (
    r"C:\Users\Lenovo\Desktop\Projects"
    r"\Christian_AI_Assistant_Assignment"
    r"\vector_store"
)

REFERENCE_LOOKUP_PATH = os.path.join(
    VECTOR_STORE_PATH,
    "reference_lookup.json"
)

# ======================================================
# EMBEDDINGS
# ======================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ======================================================
# LOAD FAISS
# ======================================================

db = FAISS.load_local(
    VECTOR_STORE_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

# ======================================================
# LOAD REFERENCE LOOKUP
# ======================================================

with open(
    REFERENCE_LOOKUP_PATH,
    "r",
    encoding="utf-8"
) as f:

    reference_lookup = json.load(f)

# ======================================================
# RETRIEVER
# ======================================================

def retrieve(
        query,
        k=3):

    query = query.strip()

    # ==================================================
    # EXACT VERSE LOOKUP
    # ==================================================

    verse_pattern = r"([1-3]?\s?[A-Za-z]+)\s+(\d+):(\d+)"

    match = re.search(
        verse_pattern,
        query,
        re.IGNORECASE
    )

    if match:

        reference = match.group(0).lower()

        if reference in reference_lookup:

            verse_data = reference_lookup[
                reference
            ]

            doc = Document(

                page_content=(
                    f"{verse_data['reference']}\n"
                    f"{verse_data['verse_text']}"
                ),

                metadata={
                    "reference":
                    verse_data["reference"]
                }
            )

            return [doc]

    # ==================================================
    # SEMANTIC SEARCH
    # ==================================================

    docs = db.similarity_search(
        query,
        k=k
    )

    return docs