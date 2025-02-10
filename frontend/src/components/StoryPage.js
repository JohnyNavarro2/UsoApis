import React, { useState } from "react";
import AudioHistory from "./AudioHistory";
import TextInput from "./TextInput";

const DJANGO_API_URL = "http://127.0.0.1:8000/api/text-to-speech/";

const StoryPage = () => {
  const [history, setHistory] = useState([]);

  const handleConvert = async (text) => {
    try {
      const response = await fetch(DJANGO_API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (response.ok) {
        const audioBlob = await response.blob();
        const audioURL = URL.createObjectURL(audioBlob);

        const newEntry = { text, audioURL };
        setHistory([newEntry, ...history]);

        const audio = new Audio(audioURL);
        audio.play();
      } else {
        console.error("Error en la conversión de texto a voz.");
      }
    } catch (error) {
      console.error("Error de conexión con el backend:", error);
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center">📖 Página de Cuentos - Texto a Voz 🎙️</h2>
      <div className="row mt-4">
        <AudioHistory history={history} />
        <TextInput onConvert={handleConvert} />
      </div>
    </div>
  );
};

export default StoryPage;
