AI Chatbot Platform (Full Stack + API + Persistent Memory)

  A production-ready AI chatbot platform with REST APIs, persistent chat storage, and scalable backend architecture.

- Live Demo:
 🔗 https://ai-chatbot-2qo0.onrender.com

- Overview:
 
  This project is a full-stack AI chatbot system that allows users to interact with an intelligent assistant powered by OpenAI.
It includes a robust Flask backend, REST APIs, database persistence, and deployment-ready configuration.

- Built with a focus on:

 Clean architecture
 Real-world backend practices
 Resume-ready engineering standards
 
 - Key Features:
 
  AI Capabilities
  Context-based chatbot responses using OpenAI API
  Dynamic prompt handling
  Fast response generation
  
 - Backend & APIs:
 
  RESTful API design
  Modular Flask architecture
  Error handling & validation
  JSON-based request/response
  
 - Data Persistence:
 - 
   SQLite database integration
    Chat history storage
    Timestamp tracking
	
 - Security:
 - 
    API key via environment variables
   No hardcoded secrets
   Safe config handling
   
 - Deployment Ready:
   
   Compatible with Render / AWS
   Environment-based configuration
   Production-ready structure
   
- Tech Stack:

Backend: Flask (Python)
AI Engine: OpenAI GPT API
Database: SQLite
Frontend: HTML, CSS, JavaScript
API Testing: Postman
Version Control: Git & GitHub
Deployment: Render / AWS

- System Architecture:
- 
Client (Browser / Postman)
        ↓
Flask Backend (app.py)
        ↓
OpenAI API  +  SQLite DB

-  API Documentation:
   1. Chat Endpoint
POST /chat
Request Body
{
  "message": "Hello AI"
}
Response
{
  "response": "Hello! How can I assist you today?"
}
 2. Health Check (Optional Enhancement)
GET /
{
  "status": "Server is running"
}

 - Database Design:
 Table: chats
CREATE TABLE chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 What it does:
Stores each conversation
Enables chat history tracking
Helps in future AI improvements (memory / analytics)

 - Project Structure:
 - 
ai-chatbot/
│
├── app.py                  # Main backend logic
├── templates/
│   └── index.html          # UI
├── static/                 # CSS / JS
├── database.db             # SQLite DB
├── requirements.txt
├── .env                    # Environment variables
└── README.md

   - Setup Instructions:
1. Clone Repo
https://github.com/navida03/ai-chatbot.git

2. Install Dependencies
pip install -r requirements.txt

 3. Configure Environment Variables
Create .env file:
OPENAI_API_KEY=your_api_key_here

 4. Run App
python app.py

-  Testing (Postman): 
Method: POST
URL: http://localhost:5000/chat
Body: JSON

 Deployment Guide
🔹 Render 
Push code to GitHub
Create new Web Service
Add:
Build Command: pip install -r requirements.txt
Start Command: python app.py
Add env variable:

Chat UI
Postman API testing
 view
 Challenges Solved
 403 / Bad Request errors → Fixed API handling
 API key setup confusion → Moved to env variables
 Chat saving → Implemented SQLite persistence
 Deployment confusion → Structured production-ready app
 
Developed a full-stack AI chatbot platform using Flask and OpenAI API with persistent chat storage using SQLite. Designed RESTful APIs, implemented secure environment configurations, and prepared the application for cloud deployment (Render/AWS).

👩‍💻 Author
Navida Rajbhoj
















