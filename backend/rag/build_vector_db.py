import os
import json
import pandas as pd

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


CSV_PATH = r"C:\Users\Lenovo\Desktop\Projects\Christian_AI_Assistant_Assignment\data\bible.csv"

VECTOR_STORE_PATH = r"C:\Users\Lenovo\Desktop\Projects\Christian_AI_Assistant_Assignment\vector_store"

os.makedirs(
    VECTOR_STORE_PATH,
    exist_ok=True
)

print("Loading Bible CSV...")

df = pd.read_csv(CSV_PATH)

df.columns = df.columns.str.strip()

print("Columns:")
print(df.columns.tolist())

documents = []
reference_lookup = {}

for _, row in df.iterrows():

    reference = (
        f"{row['book_name']} "
        f"{row['chapter_number']}:"
        f"{row['verse_number']}"
    )

    verse_text = str(
        row["verse_text"]
    )

    document = Document(
        page_content=(
            f"{reference}\n"
            f"{verse_text}"
        ),
        metadata={
            "reference": reference,
            "book": row["book_name"],
            "book_number": int(row["book_number"]),
            "chapter": int(row["chapter_number"]),
            "verse": int(row["verse_number"]),
            "testament": row["testament_name"],
            "testament_abbr": row["testament_abbr"],
            "version": row["version_abbr"]
        }
    )

    documents.append(document)

    reference_lookup[
        reference.lower()
    ] = {
        "reference": reference,
        "verse_text": verse_text
    }

print(f"Documents Created: {len(documents)}")

# Save lookup

with open(
    os.path.join(
        VECTOR_STORE_PATH,
        "reference_lookup.json"
    ),
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        reference_lookup,
        f,
        indent=4,
        ensure_ascii=False
    )

print("Loading embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating FAISS...")

vector_db = FAISS.from_documents(
    documents,
    embeddings
)

vector_db.save_local(
    VECTOR_STORE_PATH
)

print("SUCCESS")
print("Vector DB Saved")
print(f"Total Documents: {len(documents)}")