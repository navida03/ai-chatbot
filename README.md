HYBRID AI CHATBOT WEB APPLICATION

A full-stack AI-powered chatbot that combines Machine Learning (Scikit-learn) with OpenAI GPT fallback to deliver intelligent and dynamic responses.

LIVE DEMO

https://ai-chatbot-2qo0.onrender.com

HOW IT WORKS

This chatbot uses a hybrid approach:
	1.	Intent Classification (ML Model)
	•	Uses TF-IDF + Scikit-learn model
	•	Matches user input to predefined intents
	•	Returns fast, rule-based responses
	2.	Confidence Check
	•	If confidence ≥ 40% → return intent response
	•	If confidence < 40% → fallback to GPT
	3.	GPT Fallback (OpenAI API)
	•	Handles unknown or complex queries
	•	Generates dynamic, human-like responses
	4.	Chat Storage
	•	Stores all conversations in SQLite database
	•	Includes message, response, intent, confidence, timestamp

 FEATURES
 
	•	 Interactive chatbot UI
	•	 ML-based intent classification
	•	 OpenAI GPT fallback for smart responses
	•	 Confidence scoring system
	•	 SQLite chat history storage
	•	 Fast API responses via Flask
	•	 Deployable on Render / AWS
	•	 Secure API key handling (env variables recommended)

 TECH STACK
	•	Backend: Flask (Python)
	•	Frontend: HTML, CSS, JavaScript
	•	ML: Scikit-learn, TF-IDF
	•	Database: SQLite
	•	AI Integration: OpenAI API
	•	Deployment: Render / AWS
	•	Version Control: Git, GitHub

  PROJECT STRUCTURE
  ai-chatbot/
│── app.py
│── intents.json
│── model.pkl
│── vectorizer.pkl
│── chat_history.db
│── templates/
│   └── index.html
│── static/
│   └── style.css
│── requirements.txt
│── runtime.txt

INSTALLATION

. Clone Repository
https://github.com/navida03/ai-chatbot.git

. OPENAI API SETUP
	1.	Go to: https://platform.openai.com/api-keys
	2.	CreateD a new API key

 Set environment variable (recommended)
export OPENAI_API_KEY="your_api_key_here"

. RUN THE APP
python3 app.py

. OPEN BROWSER
http://127.0.0.1:5000

. API ENDPOINT

POST/chat

{
   "message: "hey"
}

Response:
{
  "response": "Hello! How can I help you today?"
}

. Database (SQLite)
Stores user messages and AI responses
Automatically created on first run
Table structure:
CREATE TABLE chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_response TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

 Author
Navida Rajbhoj
GitHub: https://github.com/navida03
  






















