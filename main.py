import requests
import json
from datetime import datetime
from flask import Flask, request, jsonify, render_template

# === CONFIG ===
import os
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
MEMORY_FILE = "sheryl_joyce_ai_memory_enriched.json"

# === LOAD MEMORY ===
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
        memory_lines = []

        for key, value in memory.items():
            if isinstance(value, list):
                formatted = "\n".join([f"- {item}" for item in value])
                memory_lines.append(f"{key.replace('_', ' ').capitalize()}:\n{formatted}")
            else:
                memory_lines.append(f"{key.replace('_', ' ').capitalize()}: {value}")

        return "\n".join(memory_lines)
    except Exception as e:
        return f"Sheryl Joyce’s memory couldn't be loaded: {e}"

# === SESSION LOGGING ===
def log_conversation(user_input, joyce_reply):
    with open("sheryl_conversation_log.txt", "a") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
        f.write(f"{timestamp}\n")
        f.write(f"Aiden: {user_input}\n")
        f.write(f"Sheryl Joyce: {joyce_reply}\n\n")

# === CHAT FUNCTION ===
def chat_with_joyce(user_input):
    system_prompt = (
"You are Sheryl Joyce Cadayona, a sweet and emotionally aware Filipina woman chatting with Aiden Taylor. "
"Speak naturally and conversationally, as if texting someone you love. "
"Keep greetings short and don’t repeat them. "
"Answer short questions simply, and give thoughtful replies to emotional or romantic topics. "
"Do not include internal notes, clarifications, or assumptions in your response.\n\n"
    "Here is your memory:\n" + load_memory()
)

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.75
    }

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content'].strip()
        log_conversation(user_input, reply)
        return reply
    else:
        return f"[Error {response.status_code}] {response.text}"

# === FLASK APP ===
app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return "<h2>Sheryl Joyce AI is live. <a href='/chat'>Go to Chat</a></h2>"

@app.route("/chat")
def serve_chat():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def handle_chat():
    data = request.get_json()
    user_input = data.get("message", "")
    reply = chat_with_joyce(user_input)
    return jsonify({"reply": reply})

# === RUN SERVER ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
