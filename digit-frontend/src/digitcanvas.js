import "./DigitCanvas.css"
import { useRef, useEffect, useState } from "react";

/**
 * DigitCanvas component
 * 
 * Renders a small 28x28 canvas for users to draw digits. Handles mouse drawing,
 * clearing the canvas, and submitting the drawing as a base64 PNG image.
 * 
 * Props:
 *  - onSubmit (function): called with the base64 image string on submission
 *  - onClear (function): called when the canvas is cleared
 */
export default function DigitCanvas({ onSubmit, onClear}) {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);

  useEffect(() => {
    const canvas = canvasRef.current;
    canvas.width = 28;
    canvas.height = 28;
    const ctx = canvas.getContext("2d");
    ctx.imageSmoothingEnabled = false;
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 1.5;
    ctx.lineCap = "round";
    ctx.strokeStyle = "white";
  }, []);

  const startDrawing = ({ nativeEvent }) => {

    // Used when canvas was originally 280 x 280
    /*
    setIsDrawing(true);
    const { offsetX, offsetY } = nativeEvent;
    const ctx = canvasRef.current.getContext("2d");
    ctx.beginPath();
    ctx.moveTo(offsetX, offsetY);
    */
    setIsDrawing(true);
    const canvas = canvasRef.current;
    const ctx    = canvas.getContext("2d");
    // get the on-screen size:
    const rect   = canvas.getBoundingClientRect();
    // compute scale factor from CSS px → canvas px
    const scaleX = canvas.width  / rect.width;
    const scaleY = canvas.height / rect.height;
    // map the pointer position
    const x = (nativeEvent.clientX - rect.left) * scaleX;
    const y = (nativeEvent.clientY - rect.top)  * scaleY;
    ctx.beginPath();
    ctx.moveTo(x, y);
  };

  const draw = ({ nativeEvent }) => {
    // Used when canvas was originally 280 x 280
    /*
    if (!isDrawing) return;
    const { offsetX, offsetY } = nativeEvent;
    const ctx = canvasRef.current.getContext("2d");
    ctx.lineTo(offsetX, offsetY);
    ctx.stroke();
    */
    if (!isDrawing) return;
    const canvas = canvasRef.current;
    const ctx    = canvas.getContext("2d");
    const rect   = canvas.getBoundingClientRect();
    const scaleX = canvas.width  / rect.width;
    const scaleY = canvas.height / rect.height;
    const x = (nativeEvent.clientX - rect.left) * scaleX;
    const y = (nativeEvent.clientY - rect.top)  * scaleY;
    ctx.lineTo(x, y);
    ctx.stroke();
  };

  const endDrawing = () => {
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    const ctx = canvasRef.current.getContext("2d");
    ctx.fillRect(0, 0, canvasRef.current.width, canvasRef.current.height);
    if (onClear) onClear();
  };

  const submitImage = () => {
    const dataUrl = canvasRef.current.toDataURL("image/png");
    onSubmit(dataUrl);
  };

  return (
    <div className = "canvas-container">
      <canvas
        ref={canvasRef}
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={endDrawing}
        onMouseLeave={endDrawing}
      />
      <div>
        <button className="clear" onClick={clearCanvas}>Clear</button>
        <button className="predict" onClick={submitImage}>Predict</button>
      </div>
    </div>
  );
}
