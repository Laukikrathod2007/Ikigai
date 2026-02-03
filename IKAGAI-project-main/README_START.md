# How to Run the App Locally

## Quick Start (Windows)

1. **Double-click `run_app.bat`** - This will start both servers automatically

OR

## Manual Start

### Step 1: Start Flask Backend
```bash
cd backend
python app.py
```
The backend will run on `http://localhost:5000`

### Step 2: Start Frontend Server (in a new terminal)
```bash
cd frontend
python -m http.server 8000
```
The frontend will run on `http://localhost:8000`

### Step 3: Open in Browser
Open: `http://localhost:8000/demo.html`

## What You'll See

- **Daily Check-In Tab**: Submit your wellness data and get stress level assessment
- **Wellness Chatbot Tab**: Chat with the AI wellness chatbot in different modes

## Troubleshooting

- If port 5000 is busy, change the port in `backend/app.py`
- If port 8000 is busy, use a different port: `python -m http.server 8080`
- Make sure Flask dependencies are installed: `pip install -r backend/requirements.txt`
