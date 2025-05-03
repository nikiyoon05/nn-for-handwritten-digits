import DigitCanvas from "./digitcanvas";

function App() {
  const handleSubmit = (imageDataUrl) => {
    console.log("Sending image:", imageDataUrl);
    // TODO: Send to backend later
  };

  return (
    <div className="App">
      <h1>Draw a digit</h1>
      <DigitCanvas onSubmit={handleSubmit} />
    </div>
  );
}

export default App;