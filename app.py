from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI()  # or pass api_key="sk-...."

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/chat")
def chat():
    user_input = request.form.get("message", "")
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",                 # or another chat-capable model
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = resp.choices[0].message.content
    except Exception as e:
        bot_reply = f"Error: {e}"
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)