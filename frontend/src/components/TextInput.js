import React, { useState } from "react";

const TextInput = ({ onConvert }) => {
  const [text, setText] = useState("");

  const handleConvertClick = () => {
    if (text.trim()) {
      onConvert(text);
      setText(""); // Limpiar el campo de texto después de convertir
    }
  };

  return (
    <div className="col-md-8">
      <div className="text-container">
        <h3>✍ Escribe tu cuento:</h3>
        <textarea
          className="form-control mb-3"
          rows="4"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>
        <button className="btn btn-success w-100" onClick={handleConvertClick}>
          🔊 Convertir a Voz
        </button>
      </div>
    </div>
  );
};

export default TextInput;
