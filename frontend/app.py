import streamlit as st
import requests


BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Christian AI Assistant",
    layout="wide"
)

st.title("✝ Christian AI Assistant")

tab1, tab2 = st.tabs(
    [
        "Chat",
        "Image Generation"
    ]
)

# ==================================
# CHAT TAB
# ==================================

with tab1:

    st.header(
        "Bible Chat"
    )

    question = st.text_input(
        "Ask a Bible Question"
    )

    if st.button(
        "Ask"
    ):

        if question.strip():

            try:

                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={
                        "question": question
                    },
                    timeout=180
                )

                if response.status_code != 200:

                    st.error(
                        f"Backend Error: "
                        f"{response.status_code}"
                    )

                    st.code(
                        response.text
                    )

                else:

                    data = response.json()

                    st.subheader(
                        "Answer"
                    )

                    st.write(
                        data.get(
                            "answer",
                            ""
                        )
                    )

                    citations = data.get(
                        "citations",
                        []
                    )

                    if citations:

                        st.subheader(
                            "References"
                        )

                        for citation in citations:

                            st.write(
                                f"• {citation}"
                            )

            except Exception as e:

                st.error(
                    str(e)
                )

# ==================================
# IMAGE TAB
# ==================================

with tab2:

    st.header(
        "Christian Image Generation"
    )

    image_prompt = st.text_input(
        "Enter Image Prompt"
    )

    if st.button(
        "Generate Image"
    ):

        if image_prompt.strip():

            try:

                response = requests.post(
                    f"{BACKEND_URL}/generate-image",
                    json={
                        "prompt":
                        image_prompt
                    },
                    timeout=600
                )

                if response.status_code != 200:

                    st.error(
                        response.text
                    )

                else:

                    data = response.json()

                    st.image(
                        data["image_path"],
                        caption=image_prompt
                    )

            except Exception as e:

                st.error(
                    str(e)
                )