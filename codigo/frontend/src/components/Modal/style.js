import styled from "styled-components";

export const ModalOverlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
`;

export const ModalContainer = styled.div`
  background: #b8c6d9;
  border-radius: 8px;
  max-width: 500px;
  width: 100%;
  font-family: 'Inter', sans-serif;
  box-sizing: border-box;
  text-align: justify;
`;

export const ModalHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  background: #2c3e50;
  color: white;
  width: 100%;
  padding: 10px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  box-sizing: border-box;  
`;

export const ModalContent = styled.div`
  p {
    margin: 10px;
  }
`;

export const CloseButton = styled.button`
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: white;
  text-align: center;
`;
