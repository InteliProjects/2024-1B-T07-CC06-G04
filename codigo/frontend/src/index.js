import React from "react";
import ReactDOM from "react-dom/client";
import "./styles/reset.css";
import "./styles/fonts/Inter.css";
import App from "./App";

const modalRoot = document.createElement("div");
modalRoot.id = "modal-root";
document.body.appendChild(modalRoot);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
