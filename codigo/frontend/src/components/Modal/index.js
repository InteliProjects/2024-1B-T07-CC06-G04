import React from "react";
import ReactDOM from "react-dom";
import { ModalOverlay, ModalContainer, ModalHeader, ModalContent, CloseButton } from "./style"; 

const Modal = ({ title, content, onClose }) => {
  return ReactDOM.createPortal(
    <ModalOverlay>
      <ModalContainer>
        <ModalHeader>
          <h2>{title}</h2>
          <CloseButton onClick={onClose}>x</CloseButton>
        </ModalHeader>
        <ModalContent>
          <p>{content}</p>
        </ModalContent>
      </ModalContainer>
    </ModalOverlay>,
    document.getElementById("modal-root") 
  );
};

export default Modal;
