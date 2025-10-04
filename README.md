Evioran AI – Public Health Chatbot

Evioran AI is an AI-driven public health awareness chatbot built using Flask and Hugging Face Transformers. It provides users with information about diseases, prevention tips, and health best practices in an interactive, conversational format.

🌟 Features

Multi-turn conversation: Remembers previous questions and responses.

Disease awareness: Answers questions about symptoms, prevention, and health advice.

Reset chat: Start a fresh conversation anytime.

Lightweight & hackathon-ready: Uses a public Hugging Face model (gpt2) with no API keys required.

Simple, clean UI: Works with index.html and style.css frontend.

💻 Tech Stack

Backend: Python, Flask

AI Model: Hugging Face Transformers (gpt2)

Frontend: HTML, CSS, JavaScript (optional enhancements)

Session Handling: Flask session for multi-turn chat

🚀 How to Run Locally

Clone the repository

git clone https://github.com/yourusername/EvioranAI.git
cd EvioranAI


Install dependencies

pip install flask transformers torch


Run the Flask app

python app.py


Open in browser
Visit: http://127.0.0.1:5000

Chat with Evioran AI!
Ask questions like:

“What are the symptoms of dengue?”

“How to prevent malaria?”

“Tips for maintaining mental health.”

📁 Project Structure
EvioranAI/
├─ app.py            # Flask backend
├─ templates/
│   └─ index.html    # Frontend HTML
├─ static/
│   └─ style.css     # CSS styling
├─ README.md         # Project documentation
├─ .gitignore

screenshots:

<img width="1920" height="1020" alt="Screenshot 2025-10-05 032127" src="https://github.com/user-attachments/assets/a1f60333-d661-40d0-b021-4e21f9275ff4" />


⚠️ Project Status – Evioran AI

Frontend:

Fully complete and polished.

Includes chat UI with multi-turn conversation, chat bubbles, reset button, and styling.

Ready for presentation/demo.

Backend:

Uses GPT-2 local via Hugging Face Transformers (pipeline("text-generation", model="gpt2")).

Functional for hackathon demos but basic AI responses only.

Needs further support for:

Smarter disease-specific answers

More advanced NLP capabilities

Handling higher traffic or multiple users simultaneously

Hackathon-ready demo:

Frontend can be fully demonstrated.

Backend AI works reliably with GPT-2; no API keys or quotas required.

📢 License

This project is for educational and hackathon purposes. Feel free to modify and enhance it!
