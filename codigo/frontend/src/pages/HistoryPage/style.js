import styled from "styled-components";

export const PageContainer = styled.div`
  width: 100%;
  height: 100vh; /* Full viewport height */
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #b8c6d9;
  overflow: auto; /* Allow scrolling */
`;

export const ContentContainer = styled.div`
  width: 80%;
  max-height: 90vh; /* Ensure it doesn't exceed the viewport height */
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: auto; /* Allow scrolling */
`;

export const TableTitle = styled.h1`
  color: #2e4e8c;
  margin-bottom: 20px;
`;
