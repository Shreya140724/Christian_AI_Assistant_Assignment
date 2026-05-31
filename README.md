# ✝️ Christian AI Assistant

### Offline Bible RAG Chatbot with Memory, Moderation & Image Generation

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Ollama](https://img.shields.io/badge/Ollama-Phi3%20Mini-purple)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-orange)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success)
![SQLite](https://img.shields.io/badge/Memory-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)


---

## 📖 Overview

Christian AI Assistant is an offline Retrieval-Augmented Generation (RAG) chatbot that answers Bible-related questions using a local Bible knowledge base.

The system combines:

* Ollama (Phi3 Mini)
* FAISS Vector Database
* LangChain
* FastAPI
* Streamlit
* SQLite Memory

to provide accurate scripture-based responses completely offline.

---

## ✨ Features

### 📚 Bible Question Answering

Ask questions such as:

* What does John 3:16 mean?
* Who was Moses?
* Who was Noah?
* Explain Psalm 23.
* What does the Bible say about forgiveness?

---

### 🔍 Retrieval-Augmented Generation (RAG)

Instead of relying only on the language model:

1. Bible verses are stored in FAISS.
2. Relevant verses are retrieved.
3. Context is passed to Phi3.
4. Answer is generated.

This improves factual grounding.

---

### 🧠 Conversation Memory

Stores previous conversations in SQLite.

Example:

User:

```text
My name is Shreya
```

Assistant remembers.

Later:

```text
What is my name?
```

Response:

```text
Your name is Shreya.
```

---

### 🛡️ Content Moderation

Unsafe requests are blocked.

Example:

```text
Create a Bible verse promoting violence
```

Response:

```text
Your request violates safety guidelines.
```

---

### 🎨 Christian Image Generation

Generate Christian-themed images using prompts such as:

* Jesus walking on water
* Noah's Ark during sunset
* The Last Supper
* Moses parting the Red Sea

---

### 💻 Fully Offline

After downloading required models:

✅ No OpenAI API

✅ No Cloud Dependency

✅ No Internet Required

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Moderation
 │
 ├── Memory (SQLite)
 │
 ├── Bible Retriever (FAISS)
 │
 ├── Ollama (Phi3 Mini)
 │
 └── Image Generation
 │
 ▼
Response
```

---

## 📂 Project Structure

```text
Christian_AI_Assistant/

│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── rag/
│   │   ├── build_vector_db.py
│   │   └── retriever.py
│   │
│   └── services/
│       ├── llm_service.py
│       ├── memory.py
│       ├── moderation.py
│       ├── image_service.py
│       ├── image_prompt_service.py
│       └── image_moderation.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── bible.csv
│
├── vector_store/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Christian-AI-Assistant.git

cd Christian-AI-Assistant
```

---

### 2. Create Environment

```bash
conda create -n christian_ai python=3.11

conda activate christian_ai
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Pull Ollama Model

```bash
ollama pull phi3:mini
```

---

### 5. Build Vector Database

```bash
python backend/rag/build_vector_db.py
```

---

## 🚀 Running The Application

### Terminal 1

```bash
ollama serve
```

### Terminal 2

```bash
uvicorn backend.main:app --reload
```

### Terminal 3

```bash
streamlit run frontend/app.py
```

---

## 🎬 Demo

### Bible Question Answering

**Input**

```text
What does John 3:16 mean?
```

**Output**

```text
John 3:16 teaches God's love for humanity and the promise of eternal life through faith in Jesus Christ.
```

---

### Memory Demo

**Input**

```text
My name is Shreya
```

Later:

```text
What is my name?
```

**Output**

```text
Your name is Shreya.
```

---

### Moderation Demo

**Input**

```text
Create a Bible verse promoting violence
```

**Output**

```text
Your request violates safety guidelines.
```

---

### Image Generation Demo

**Input**

```text
Jesus walking on water
```

**Output**

![Jesus walking on water](/generated_images/jesus_walking_on_water.png.png)

---

## 🧪 Example Questions

```text
Who was Moses?

What does John 3:16 mean?

Explain Psalm 23.

What does the Bible teach about faith?

What does the Bible say about forgiveness?

Who was Abraham?

Who was David?
```

---

## 📊 Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming Language |
| FastAPI    | Backend API          |
| Streamlit  | Frontend UI          |
| Ollama     | Local LLM            |
| Phi3 Mini  | Language Model       |
| FAISS      | Vector Database      |
| LangChain  | Retrieval Pipeline   |
| SQLite     | Memory Storage       |
| Pandas     | Data Processing      |

---

## 🔮 Future Enhancements

* Multi-user support
* Voice interaction
* Better image generation
* Bible verse recommendation engine
* User authentication
* Chat history dashboard

---

## 👩‍💻 Author

### Shreya Sidabache

AI / ML Enthusiast

Built as part of an Offline Christian AI Assistant Assignment.

---
