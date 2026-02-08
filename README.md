GenAI Security Helper

GenAI Security Helper is a web-based application designed to analyze source code snippets and provide security feedback using Generative AI. The system helps developers identify vulnerabilities, understand potential risks, and receive suggestions for improving code security.

This project consists of a Python backend API and a React frontend interface, maintained within a single repository.

Project Overview

The application allows users to:

Submit code snippets for analysis

Detect possible security issues

Receive AI-generated recommendations

Improve secure coding practices

The backend communicates with a Generative AI model to analyze the submitted code and returns structured results to the frontend.

Repository Structure
assign3/
│
├── backend/                # Python Backend (API Service)
│   ├── main.py             # Main server file
│   ├── requirements.txt    # Python dependencies
│
├── frontend/               # React Frontend Application
│
├── .gitignore              # Git ignored files configuration
└── README.md               # Project documentation

Technology Stack
Backend

Python

FastAPI / Flask (depending on your implementation)

Uvicorn (ASGI server)

Google Generative AI API

Frontend

React.js

JavaScript

HTML/CSS

Prerequisites

Before running the project, ensure you have installed:

Python (3.9 or above recommended)

Node.js (v16+ recommended)

npm

Git

Backend Setup Instructions
Step 1: Navigate to Backend Directory
cd backend

Step 2: Create Virtual Environment
python -m venv venv

Step 3: Activate Virtual Environment

Windows:

venv\Scripts\activate


Linux/macOS:

source venv/bin/activate

Step 4: Install Dependencies
pip install -r requirements.txt

Step 5: Set API Key (IMPORTANT)

Create an environment variable for your Generative AI API key:

Windows (PowerShell):

setx GOOGLE_API_KEY "your_api_key_here"


Linux/macOS:

export GOOGLE_API_KEY="your_api_key_here"


Restart terminal after setting environment variable.

Step 6: Run Backend Server

uvicorn main:app --reload


Backend will run at:

http://127.0.0.1:8000


Frontend Setup Instructions
Step 1: Navigate to Frontend Directory
cd frontend

Step 2: Install Dependencies
npm install

Step 3: Start React Application
npm start


Frontend will run at:

http://localhost:3000

API Endpoint
Analyze Code

POST /analyze-code

Request Body (JSON)
{
  "code": "print('Hello World')"
}

Response
{
  "result": "AI generated security analysis"
}

Features

AI-powered code analysis

Security vulnerability detection

Developer-friendly UI

Real-time feedback

RESTful API design

Git Configuration Notes

.gitignore is located in the project root.

venv/ and node_modules/ are excluded from version control.

