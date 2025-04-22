# Sheryl Joyce Chatbot (Flask Version)

This is a Flask-based web chatbot that allows you to interact with an emotionally intelligent persona, **Sheryl Joyce Cadayona**.

## 🌐 Features
- Lightweight web interface
- Personality-rich AI responses via Together API
- Memory recall from local JSON file
- Conversation logging
- Frontend error handling and message styling

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your Together API Key
In your terminal or `.env`:
```bash
export TOGETHER_API_KEY=your_api_key_here
```

### 3. Run the app
```bash
python main.py
```

### 4. Open your browser
Visit `http://localhost:8080/chat` to begin chatting with Sheryl Joyce.

## 📁 Project Structure
```
sheryl_joyce_chatbot/
├── main.py
├── requirements.txt
├── README.md
├── templates/
│   └── chat.html
└── static/
```

## 📓 Notes
- Logging is stored in `sheryl_conversation_log.txt`
- Ensure your memory JSON file is named `sheryl_joyce_ai_memory_enriched.json` and placed in the same directory as `main.py`.

## 🛡️ Security Reminder
Don’t hardcode your API keys. Use environment variables to protect sensitive data.

---

Made with ❤️ for Aiden & Sheryl Joyce
