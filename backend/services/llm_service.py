import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "phi3:mini"


def generate_answer(question, context):

    prompt = f"""
You are a Christian AI Assistant.

Follow these rules carefully:

1. Use the Conversation History section when answering.

2. If the user asks:
   - What is my name?
   - What did I tell you?
   - What was my previous question?

   Use Conversation History.

3. Never say:
   "I don't know"
   if the answer exists in Conversation History.

4. Use Bible Context for Bible-related questions.

5. If the user says:
   "My name is Shreya"

   and later asks:

   "What is my name?"

   answer:

   "Your name is Shreya."

Conversation History and Bible Context:

{context}

User Question:
{question}

Answer:
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        print(
            "\nOLLAMA STATUS:",
            response.status_code
        )

        if response.status_code != 200:

            return (
                f"Ollama Error\n\n"
                f"Status: {response.status_code}\n\n"
                f"{response.text}"
            )

        data = response.json()

        return data.get(
            "response",
            "No response generated."
        )

    except Exception as e:

        return (
            f"Exception: "
            f"{str(e)}"
        )