# Handwritten Digit Recognition Web App

Frontend deployed: https://nn-for-handwritten-digits-frontend.onrender.com/

A full-stack application that lets users draw digits in their browser and have them recognized by a neural network trained on the MNIST dataset. The project includes a React frontend with a drawing canvas and a Flask backend that preprocesses the image and returns the predicted digit.

![Screenshot 2025-05-03 at 2 40 38 AM](https://github.com/user-attachments/assets/651ad640-55ff-445c-973d-71282ffc57d1)

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


2. **Install backend dependencies**

   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate   # (or venv/Scripts/activate on Windows)
   pip install -r requirements.txt
   ```

3. **Prepare the frontend scaffold**

   * If you used Create React App, `digit-frontend/` should already contain `package.json`, `public/`, and `src/`.
   * Otherwise, initialize a new React project:

     ```bash
     cd digit-frontend
     npm init -y
     npm install react react-dom
     ```

4. **Install frontend dependencies**

   ```bash
   cd digit-frontend
   npm install
   ```

5. **Download MNIST data** (for training only)
   Place the official MNIST `.idx3-ubyte` and `.idx1-ubyte` files into a `data/` folder at the project root.

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

