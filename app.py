# app.py
from flask import Flask, render_template, request, jsonify, session
import requests

# -------------------------
# SET YOUR HUGGING FACE API KEY HERE
# -------------------------
HF_API_KEY = "SET YOUR HUGGING FACE API KEY HERE"  # <-- Replace with your actual key

if not HF_API_KEY:
    raise RuntimeError("Set your HF_API_KEY in the code before running!")

# Model to use
MODEL = "tiiuae/falcon-7b-instruct"


# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "supersecretkey123"  # For sessions

# Ensure chat history exists
def ensure_history():
    if "history" not in session:
        session["history"] = ["You are Evioran AI, a helpful public health awareness assistant."]

# Home route
@app.route("/")
def index():
    ensure_history()
    return render_template("index.html")  # Use your existing index.html

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    ensure_history()
    user_msg = request.form.get("message", "").strip()
    if not user_msg:
        return jsonify({"error": "empty message"}), 400

    history = session["history"]
    history.append(f"User: {user_msg}")
    prompt = "\n".join(history) + "\nAssistant:"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 200, "temperature": 0.2},
    }

    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{MODEL}",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        output = response.json()

        # Safely extract generated text
        if isinstance(output, list) and "generated_text" in output[0]:
            bot_reply = output[0]["generated_text"][len(prompt):].strip()
        elif isinstance(output, dict) and "error" in output:
            return jsonify({"error": f"Hugging Face API error: {output['error']}"}), 500
        else:
            bot_reply = "Sorry, I could not generate a response."

    except Exception as e:
        print("Error in Hugging Face API:", e)
        return jsonify({"error": "Failed to get response from AI."}), 500

    # Update history
    history.append(f"Assistant: {bot_reply}")
    session["history"] = history

    return jsonify({"reply": bot_reply})

# Reset chat history
@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"ok": True})

# Run app
if __name__ == "__main__":
    app.run(debug=True)
