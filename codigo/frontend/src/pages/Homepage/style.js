import styled from "styled-components";

export const PageContainer = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
`;

export const LeftContainer = styled.div`
  width: 50%;
  height: 100vh;
  background-color: #2e4e8c;
  display: flex;
  align-items: center;
  justify-content: center;

  img {
    width: 50%;
  }
`;

export const RightContainer = styled.div`
  width: 50%;
  height: 100vh;
  background-color: #b8c6d9;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
`;

export const ButtonContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
`;

export const UploadCsvInput = styled.input`
  background-color: red;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
`;

export const UploadContainer = styled.div`
  width: 50%;
  height: 30vh;
  border: 2px solid #141f40;
  border-radius: 6px;
  display: flex;
  align-items: stretch;
  padding-top: 30px;
  box-sizing: border-box;
  justify-content: center;
  color: #141f40;
  flex-wrap: wrap;
  cursor: pointer;

  p {
    text-align: center;
    width: 100%;
  }
`;
