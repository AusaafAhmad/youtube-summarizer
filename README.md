# 📺 YouTube Summarizer

A Python-based application that takes a YouTube video transcript and generates a structured, human-readable summary using large language models.

---

## ✨ Features

- 📄 Parses raw YouTube video transcripts  
- 🧠 Summarizes using LLMs (Ollama-compatible)  
- 📌 Outputs structured summaries with:
  - Channel Name (if available)
  - Video Title
  - Key bullet points
  - Final conclusion  
- 🔧 Easy to configure and extend

---

## 📁 Project Structure

```
youtube-summarizer/
│
├── app.py           # Main entry point
├── model.py         # LLM wrapper (Ollama or similar)
├── transcript.py    # Transcript preprocessing and formatting
├── requirements.txt # Python dependencies
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`
- [Ollama](https://ollama.com/) installed locally (or modify for your LLM provider)
- Optional: GitHub CLI or other API integrations for transcript fetching

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

1. Make sure you have a YouTube transcript available (plain text).
2. Run the summarizer:

```bash
python app.py
```

3. Output will be printed or saved depending on your configuration.

---

## 🔧 Configuration

Modify `model.py` to select your desired language model (e.g., `deepseek`, `mistral`, etc.) via the Ollama API.

Example setup:

```python
from langchain_ollama.llms import OllamaLLM
model = OllamaLLM(model="deepseek")
```

---

## ✅ Output Format Example

```
- Name of Channel: Veritasium
- Title of the Summary: Why Time Moves Forward (and Not Backward)
- Main Summary:
  • **Entropy increases** is why time appears to move forward.
  • **Time symmetry in physics laws** contradicts human experience.
  • **Arrow of time** is emergent, not fundamental.
- Final Conclusion: The direction of time is linked to entropy, not the fundamental laws of physics.
```

---

## 🛠️ TODOs & Improvements

- 🔍 Auto-fetch transcripts via YouTube API  
- 🌍 Support multilingual transcripts  
- 🧪 Add unit tests for each module  
- 🖥️ Optional web UI using Streamlit or Flask

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project  
2. Create your feature branch (`git checkout -b feature/summarization-format`)  
3. Commit your changes  
4. Push to the branch  
5. Open a pull request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Ausaaf Ahmad**  
GitHub: [@AusaafAhmad](https://github.com/AusaafAhmad)
