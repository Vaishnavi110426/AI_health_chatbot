# app.py
from flask import Flask, render_template, request, jsonify, session
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "supersecretkey123"  # for session management

# Initialize Hugging Face text-generation pipeline (GPT-2, public, free)
generator = pipeline("text-generation", model="gpt2")

# Ensure chat history exists
def ensure_history():
    if "history" not in session:
        session["history"] = ["You are Evioran AI, a helpful public health awareness assistant."]

# Home route
@app.route("/")
def index():
    ensure_history()
    return render_template("index.html")  # your existing frontend

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    ensure_history()
    user_msg = request.form.get("message", "").strip()
    if not user_msg:
        return jsonify({"error": "empty message"}), 400

    # Update history
    history = session["history"]
    history.append(f"User: {user_msg}")
    prompt = "\n".join(history) + "\nAssistant:"

    try:
        output = generator(prompt, max_length=len(prompt.split()) + 50, do_sample=True, temperature=0.7)
        bot_reply = output[0]['generated_text'][len(prompt):].strip()
    except Exception as e:
        print("Error generating text:", e)
        return jsonify({"error": "Failed to get response from AI."}), 500

    # Save bot reply in history
    history.append(f"Assistant: {bot_reply}")
    session["history"] = history

    return jsonify({"reply": bot_reply})

# Reset chat history
@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"ok": True})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

