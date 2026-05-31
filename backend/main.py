from fastapi import FastAPI
from pydantic import BaseModel

from backend.rag.retriever import retrieve
from backend.services.llm_service import generate_answer
from backend.services.memory import save_message, get_memory
from backend.services.moderation import is_safe
from backend.services.image_service import generate_image


app = FastAPI()


class ChatRequest(BaseModel):
    question: str


class ImageRequest(BaseModel):
    prompt: str


@app.get("/")
def root():

    return {
        "message": "Christian AI Assistant Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    question = request.question.strip()

    # =====================================
    # MODERATION
    # =====================================

    if not is_safe(question):

        return {
            "answer": "Your request violates safety guidelines.",
            "citations": []
        }

    # =====================================
    # MEMORY
    # =====================================

    user_id = "default_user"

    previous_messages = get_memory(user_id)

    memory_context = ""

    for message in previous_messages:

        memory_context += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    # =====================================
    # RETRIEVER
    # =====================================

    docs = retrieve(question)

    bible_context = ""

    citations = []

    for doc in docs:

        bible_context += (
            doc.page_content +
            "\n\n"
        )

        citations.append(
            doc.metadata.get(
                "reference",
                "Unknown Reference"
            )
        )

    # =====================================
    # FINAL CONTEXT
    # =====================================

    final_context = f"""
Conversation History:

{memory_context}

Bible Context:

{bible_context}
"""

    # =====================================
    # DEBUG MEMORY
    # =====================================

    print("\n========== MEMORY ==========")
    print(memory_context)
    print("============================\n")

    # =====================================
    # GENERATE ANSWER
    # =====================================

    answer = generate_answer(
        question,
        final_context
    )

    # =====================================
    # SAVE MEMORY
    # =====================================

    save_message(
        user_id,
        "user",
        question
    )

    save_message(
        user_id,
        "assistant",
        answer
    )

    # =====================================
    # RETURN RESPONSE
    # =====================================

    return {
        "answer": answer,
        "citations": citations
    }


@app.post("/generate-image")
def create_image(request: ImageRequest):

    image_path = generate_image(
        request.prompt
    )

    return {
        "image_path": image_path
    }