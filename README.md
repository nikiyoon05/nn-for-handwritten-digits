Handwritten Digit Recognition Web App

A full‑stack application that lets users draw digits in their browser and have them recognized by a neural network trained on the MNIST dataset. The project includes a React frontend with a drawing canvas and a Flask backend that preprocesses the image and returns the predicted digit.

🚀 Features

Interactive Drawing Canvas: Draw digits with smooth strokes in the browser.

Real‑Time Prediction: Click Predict to send your drawing to the backend and get an instant result.

Clear & Reset: Erase the canvas and reset the prediction display with a single click.

Submission History: (Optional) View past predictions via a /history endpoint.

Deployable: Ready for deployment on Netlify/Vercel (frontend) and Render/Heroku (backend).

🗂️ Project Structure

nn-for-handwritten-digits/
├── digit-frontend/        # React application
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── digitcanvas.js
│       ├── App.css
│       └── DigitCanvas.css
├── backend/               # Flask server
│   ├── app.py
│   └── requirements.txt
└── src/                   # Model and preprocessing
    └── Model/
        ├── neural_network.py
        ├── predict.py
        └── model.pkl      # (ignored in .gitignore)

🛠️ Tech Stack

Frontend: React, HTML5 Canvas API

Backend: Python, Flask, Flask‑CORS, Pillow, NumPy

Model: Custom neural network trained on MNIST (Python pickle)

💾 Prerequisites

Node.js & npm (v14+)

Python (3.8+)

pip (Python package manager)

⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/your‑username/nn‑for‑handwritten‑digits.git
cd nn‑for‑handwritten‑digits

2. Install the backend dependencies

cd backend
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Install the frontend dependencies

cd ../digit-frontend
npm install

▶️ Running Locally

Backend

cd backend
# development mode with hot‑reload
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

By default, the server listens at http://localhost:5001 (or port specified in app.py).

Frontend

cd digit-frontend
npm start

This will open http://localhost:3000 in your browser.

📡 API Endpoints

POST /predict

Request body: { "image": "data:image/png;base64,..." }

Response: { "prediction": <digit> }

GET /history

Response: { "history": [ { "image": "...", "prediction": <digit> }, ... ] }

GET /ping

Response: { "message": "pong" }

🚀 Deployment

Frontend build:

cd digit-frontend
npm run build

Host the contents of build/ on Netlify, Vercel, or any static‑site host.

Backend deploy:

Create a requirements.txt and a Procfile:

web: gunicorn app:app --bind 0.0.0.0:$PORT

Push to Render, Heroku, or similar.

Update your frontend’s API URL in App.js to point at the production backend.

🤝 Contributing

Feel free to open issues or pull requests. Suggestions for improvement (UI, UX, model accuracy) are welcome!
