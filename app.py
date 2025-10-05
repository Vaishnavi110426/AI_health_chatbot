# app.py
from flask import Flask, render_template, request, jsonify, session
from transformers import pipeline

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "supersecretkey123"

# Load model
generator = pipeline("text-generation", model="gpt2")

def ensure_history():
    if "history" not in session:
        session["history"] = []

@app.route("/")
def index():
    ensure_history()
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    ensure_history()
    user_msg = request.form.get("message", "").strip()

    if not user_msg:
        return jsonify({"error": "empty message"}), 400

    history = session["history"]
    history.append(f"User: {user_msg}")

    # Build compact prompt
    prompt = (
        "You are Evioran AI, a helpful public health awareness assistant.\n"
        "Provide useful, accurate, and simple health advice.\n\n"
        + "\n".join(history[-4:])  # keep only last few turns
        + "\nAssistant:"
    )

    try:
        output = generator(prompt, max_length=150, do_sample=True, temperature=0.7)
        bot_reply = output[0]["generated_text"].split("Assistant:")[-1].strip()
    except Exception as e:
        print("Error generating text:", e)
        return jsonify({"error": "Failed to get response from AI."}), 500

    history.append(f"Assistant: {bot_reply}")
    session["history"] = history

    return jsonify({"reply": bot_reply})

@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)

