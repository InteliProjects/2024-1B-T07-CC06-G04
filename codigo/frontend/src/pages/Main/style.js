import styled from 'styled-components';

export const Header = styled.div`
  width: 100%;
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px; 
  background-color: #2c3e50;
  color: white;
  font-family: 'Inter', sans-serif;
  font-size: 1em;
  box-sizing: border-box;

  .logo-container {
    display: flex;
    align-items: center;

    img {
      width: 80px;
      height: auto;
      margin-right: 10px; 
    }

    h2 {
      margin: 0;
    }
  }

  h2:last-child {
    margin: 0;
    margin-right: 30px;
  }
`;

export const Container = styled.div`
  display: flex;
  flex-direction: row;
  background-color: #b8c6d9;
  font-family: 'Inter', sans-serif;
  height: calc(100vh - 70px); /* Full viewport height minus header */
`;

export const LeftPanel = styled.div`
  width: 30%;
  padding: 20px;
  background-color: #b8c6d9;
  display: flex;
  flex-direction: column;
  gap: 10px;
  overflow-y: auto;

  select,
  input {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box; 
  }
`;

export const RightPanel = styled.div`
  width: 70%;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #d1e0f0;
  overflow-y: auto;
`;

export const Map = styled.div`
  width: 100%;
  height: 100%; /* Full height of the parent container */
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #2e4e8c;
  border-radius: 4px;
  background-color: white;
  margin-top: 20px;

  img {
    max-width: 100%; 
    height: 100%;
  }
`;

export const Result = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 95%;
  margin-top: 10px;
  padding: 20px;
  background-color: #e8eff7;
  border: 2px solid #2e4e8c;
  border-radius: 4px;
`;

export const SuccessMessage = styled.div`
  width: 100%;
  text-align: center;

  h3 {
    font-weight: bold;
  }

  p {
    margin: 5px 0;
  }
`;

export const DownloadContainer = styled.div`
  width: 40%;
  height: 18vh;
  border: 2px solid #141f40;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  cursor: pointer;

  p {
    text-align: center;
    width: 100%;
    font-family: 'Inter', sans-serif;
    margin-top: 10px; 
  }
`;

export const DownloadButton = styled.button`
  color: black;
  border: none;
  background: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.5em;
  margin-bottom: 10px; 
`;

export const UploadContainer = styled.div`
  width: 90%;
  height: 18vh;
  border: 2px solid #141f40;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  box-sizing: border-box;
  color: #141f40;
  cursor: pointer;
  margin-top: 20px;

  p {
    text-align: center;
    width: 100%;
  }
`;