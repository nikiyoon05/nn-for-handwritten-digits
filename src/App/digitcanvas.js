import { useRef, useEffect, useState } from "react";

export default function DigitCanvas({ onSubmit }) {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);

  useEffect(() => {
    const canvas = canvasRef.current;
    canvas.width = 280;
    canvas.height = 280;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 20;
    ctx.lineCap = "round";
    ctx.strokeStyle = "white";
  }, []);

  const startDrawing = ({ nativeEvent }) => {
    setIsDrawing(true);
    const { offsetX, offsetY } = nativeEvent;
    const ctx = canvasRef.current.getContext("2d");
    ctx.beginPath();
    ctx.moveTo(offsetX, offsetY);
  };

  const draw = ({ nativeEvent }) => {
    if (!isDrawing) return;
    const { offsetX, offsetY } = nativeEvent;
    const ctx = canvasRef.current.getContext("2d");
    ctx.lineTo(offsetX, offsetY);
    ctx.stroke();
  };

  const endDrawing = () => {
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    const ctx = canvasRef.current.getContext("2d");
    ctx.fillRect(0, 0, canvasRef.current.width, canvasRef.current.height);
  };

  const submitImage = () => {
    const dataUrl = canvasRef.current.toDataURL("image/png");
    onSubmit(dataUrl);
  };

  return (
    <div>
      <canvas
        ref={canvasRef}
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={endDrawing}
        onMouseLeave={endDrawing}
        style={{ border: "1px solid #ccc", backgroundColor: "black", display: "block", margin: "auto" }}
      />
      <div>
        <button onClick={clearCanvas}>Clear</button>
        <button onClick={submitImage}>Predict</button>
      </div>
    </div>
  );
}
