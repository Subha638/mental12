from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face DialoGPT model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

# Crisis words
crisis_words = ["suicide", "self-harm", "kill myself", "hopeless"]

# ---------------- ROUTES ----------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/help")
def help_page():
    return render_template("help.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ---------------- CHAT API ----------------
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["message"]

    # Crisis word check
    if any(word in user_input.lower() for word in crisis_words):
        reply = "⚠️ It seems you’re in distress. Please reach out immediately: Call 988 (Suicide & Crisis Lifeline)."
    else:
        response = chatbot(user_input, max_new_tokens=100, pad_token_id=50256)
        reply = response[0]["generated_text"].replace(user_input, "").strip()

    return jsonify({"reply": reply})

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
