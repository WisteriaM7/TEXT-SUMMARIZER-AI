# 📝 LLaMA Text Summarizer

A simple AI-powered text summarization app using a **locally hosted LLaMA model** via Ollama, with a FastAPI backend and a Streamlit frontend.
![text summarizer](https://github.com/WisteriaM7/TEXT-SUMMARIZER-AI/blob/main/Screenshot%202026-04-25%20201433.png)
---

## 🧠 Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| LLM       | LLaMA 2 (via Ollama)    |
| Backend   | FastAPI + Uvicorn       |
| Frontend  | Streamlit               |
| Language  | Python 3.10+            |

---

## 📁 Project Structure

```
text-summarizer-llama/
│
├── backend/
│   ├── __init__.py
│   └── main.py          # FastAPI app
│
├── frontend/
│   └── app.py           # Streamlit UI
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/WisteriaM7/TEXT-SUMMARIZER-AI.git
cd TEXT-SUMMARIZER-AI
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama & Pull the LLaMA Model

- Download Ollama from: https://ollama.com
- Pull the model:

```bash
ollama pull llama2
```

---

## 🚀 Running the App

Open **two separate terminals**:

**Terminal 1 — Start the Backend:**

```bash
uvicorn backend.main:app --reload
```

Backend runs at: `http://localhost:8000`

**Terminal 2 — Start the Frontend:**

```bash
streamlit run frontend/app.py
```

Frontend runs at: `http://localhost:8501`

---

## 📌 API Endpoints

| Method | Endpoint      | Description              |
|--------|---------------|--------------------------|
| GET    | `/`           | Health check             |
| POST   | `/summarize/` | Summarize submitted text |

---

## ✅ Features

- Local LLM inference — no API keys, no internet needed
- Clean Streamlit UI with error handling
- FastAPI backend with CORS support
- Easily extendable to other Ollama models

---

## 🛠️ Troubleshooting

- **Backend not connecting?** Make sure `uvicorn backend.main:app --reload` is running.
- **Ollama errors?** Run `ollama serve` in a separate terminal and verify with `ollama list`.
- **Slow responses?** LLaMA 2 runs locally — speed depends on your CPU/GPU.
