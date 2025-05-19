# YouTube Video Summarizer with Ollama

This project summarizes YouTube videos locally using Ollama and open-source LLMs. It extracts transcripts via captions or audio transcription (OpenAI Whisper) and generates concise summaries using LangChain prompt templates.

## Setup & Usage

1. Install Ollama ([https://ollama.com/download](https://ollama.com/download))  
2. Clone repo and install dependencies:  
```
git clone https://github.com/AusaafAhmad/youtube-summarizer.git
cd youtube-summarizer
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Pull your preferred model:  
```
ollama pull <model-name>
```

4. Run Ollama server:  
```
ollama serve
```

5. Launch the app:  
```
streamlit run app.py
```

For detailed explanation, architecture, and future plans, see the Medium article:  
[How I Built a YouTube Summarizer Using Ollama](https://medium.com/p/86bbb3194b6c)
