# 🤖 J.A.R.V.I.S – Your Personal AI Voice Assistant

J.A.R.V.I.S (Just A Rather Very Intelligent System) is an advanced AI voice assistant inspired by Iron Man's Jarvis. This project uses speech recognition and text-to-speech to interact with users and perform intelligent tasks using LLMs.

---

## 🧠 Features

- 🎤 Speech-to-text using Whisper (or other models)
- 🗣️ Text-to-speech with ElevenLabs integration
- 🤖 Smart response generation using Groq LLM (Mixtral, LLaMA, etc.)
- 💾 Saves output audio responses
- 🧩 Modular structure for easy extension
- 💻 Simple terminal-based UI (ready to extend to GUI)

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
 git clone https://github.com/Akashgite1/J.A.R.V.I.S-Your-Personal-AI-Voice-Assistant.git cd J.A.R.V.I.S-Your-Personal-AI-Voice-Assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Setup API Keys
```bash                 
Create a .env file in the root directory:
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```
### 4. Usage🎯 
```bash
Run J.A.R.V.I.S
python main.py
```

### Tech Stack 🛠
```bash
Python 🐍
Groq LLM API (Mixtral, LLaMA)
ElevenLabs Text-to-Speech
FFmpeg (for audio processing)
Whisper (for STT)
PyAudio 
```
```bash
📁 Project Structure

├── main.py                  # Entry point
├── speech_to_text.py        # Converts voice to text
├── groq_llm.py              # Handles response generation
├── elevenlabs_tts.py        # Converts text to speech
├── utils/                   # Utility scripts
├── requirements.txt
└── README.md
```
```
⭐️ Support

If you find this project helpful, consider giving it a ⭐ on GitHub!
```
