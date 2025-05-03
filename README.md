# Handwritten Digit Recognition Web App

A full-stack application that lets users draw digits in their browser and have them recognized by a neural network trained on the MNIST dataset. The project includes a React frontend with a drawing canvas and a Flask backend that preprocesses the image and returns the predicted digit.

## Features

* **Interactive Drawing Canvas**: Draw digits with smooth strokes in the browser.
* **Real-Time Prediction**: Click **Predict** to send your drawing to the backend and get an instant result.
* **Clear & Reset**: Erase the canvas and reset the prediction display with a single click.
* **Submission History**: (Optional) View past predictions via a `/history` endpoint.
* **Deployable**: Ready for deployment on Netlify/Vercel (frontend) and Render/Heroku (backend).

## Project Structure

```
nn-for-handwritten-digits/
├── saved_model.pkl        # trained model (ignored via .gitignore)
├── digit-frontend/          # React application
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── digitcanvas.js
│       ├── App.css
│       └── DigitCanvas.css
├── backend/                 # Flask server
│   ├── app.py
│   └── requirements.txt
└── src/                     # Model and preprocessing code
    └── Model/
        ├── neural_network.py
        ├── predict.py
        ├── load_data.py
        ├── train.py
```

nn-for-handwritten-digits/
├── digit-frontend/          # React application
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── digitcanvas.js
│       ├── App.css
│       └── DigitCanvas.css
├── backend/                 # Flask server
│   ├── app.py
│   └── requirements.txt
└── src/                     # Model and preprocessing code
└── Model/
├── neural\_network.py
├── predict.py
└── model.pkl        # (ignored via .gitignore)

````

## Tech Stack

- **Frontend**: React, HTML5 Canvas API
- **Backend**: Python, Flask, Flask-CORS, Pillow, NumPy
- **Model**: Custom neural network trained on MNIST

## Prerequisites

- **Node.js** & **npm** (v14+)
- **Python** (3.8+)
- **pip**

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/nn-for-handwritten-digits.git
   cd nn-for-handwritten-digits
````

2. **Install backend dependencies**

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies**

   ```bash
   cd ../digit-frontend
   npm install
   ```

## Running Locally

### Backend

```bash
cd backend
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port=5001
```

### Frontend

```bash
cd digit-frontend
npm start
```

Open `http://localhost:3000` in your browser.

## API Endpoints

* **POST** `/predict`
  Request body: `{ "image": "data:image/png;base64,..." }`
  Response: `{ "prediction": <digit> }`

* **GET** `/history`
  Response: `{ "history": [ { "image": "...", "prediction": <digit> }, ... ] }`

* **GET** `/ping`
  Response: `{ "message": "pong" }`

## Deployment

### Frontend (Netlify or Vercel)

1. Build:

   ```bash
   cd digit-frontend
   npm run build
   ```
2. Deploy the `build/` folder on Netlify or Vercel.

### Backend (Render or Heroku)

1. Ensure you have a `requirements.txt` and a `Procfile`:

   ```text
   web: gunicorn app:app --bind 0.0.0.0:$PORT
   ```
2. Push the `backend/` folder to Render or Heroku.
3. Update the frontend's API URL in `App.js` to point to your production backend.

## Contributing

Feel free to open issues or pull requests. Suggestions for UI, UX, or model improvements are welcome.


