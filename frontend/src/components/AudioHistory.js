import React from "react";

const AudioHistory = ({ history }) => {
  return (
    <div className="col-md-4">
      <h4>🎵 Historial de Audios</h4>
      <ul className="list-group audio-list">
        {history.length === 0 && <li className="list-group-item">No hay audios aún.</li>}
        {history.map((item, index) => (
          <li key={index} className="list-group-item d-flex justify-content-between align-items-center">
            <span>{item.text.substring(0, 20)}...</span>
            <button className="btn btn-sm btn-primary" onClick={() => new Audio(item.audioURL).play()}>
              ▶ Reproducir
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AudioHistory;
