// App.js
import { useState } from "react";
import DigitCanvas from "./digitcanvas";
import "./App.css";

function App() {
  // Stores the digit prediction returned by the backend
  const [numPrediction, setNumPrediction] = useState(null);

  // Called when the user submits a drawing
  const handleSubmit = async (imageDataUrl) => {
    try {
      const apiUrl = process.env.REACT_APP_API_URL || "http://localhost:5001";
      const response = await fetch(`${apiUrl}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: imageDataUrl }),
      });

      const data = await response.json();
      console.log("Prediction:", data.prediction);

      // Update state with the predicted digit
      setNumPrediction(data.prediction);
    } catch (error) {
      console.error("Prediction request failed:", error);
      // Optionally show an error message in the UI
    }
  };

  // Clear prediction (when canvas is cleared)
  const handleClearPrediction = () => {
    setNumPrediction(null);
  };

  return (
    <div className="app">
      <h1 id="introduction">
        Hello! This is a neural network built from scratch by{" "}
        <span className="author">Niki Yoon</span> to recognize handwritten digits!
      </h1>

      <p id="description">
        Click{" "}
        <a href="https://github.com/nikiyoon05/nn-for-handwritten-digits" target="_blank" rel="noopener noreferrer">
          here
        </a>{" "}
        to check out the code on GitHub.
      </p>

      <div className="overallcanvas">
        <header>
          Draw a digit:
          <DigitCanvas onSubmit={handleSubmit} onClear={handleClearPrediction} />
        </header>

        {/* Show predicted digit if available */}
        <p id="guess">
          I predict your number to be:{" "}
          {numPrediction !== null ? (
            <span className="prediction">{numPrediction}</span>
          ) : (
            <em className="prediction">?</em>
          )}
        </p>
      </div>
    </div>
  );
}

export default App;
