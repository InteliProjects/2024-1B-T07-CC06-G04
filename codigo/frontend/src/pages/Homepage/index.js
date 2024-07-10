import React from "react";
import { useNavigate } from "react-router-dom";
import Logo from "../../assets/logo-aegis.png";
import { PrimaryButton } from "../../components/Buttons/style";
import {
  ButtonContainer,
  PageContainer,
  RightContainer
} from "./style";

function Homepage() {
  const navigate = useNavigate(); // Hook para navegação

  // Função para navegar para a página principal
  const handleStartClick = () => {
    navigate("/main");
  };

  return (
    <PageContainer>
      <RightContainer>
        <img src={Logo} alt="Logo" />
      </RightContainer>
      <RightContainer>
        <ButtonContainer>
          <PrimaryButton onClick={handleStartClick}>Começar</PrimaryButton>
        </ButtonContainer>
      </RightContainer>
    </PageContainer>
  );
}

export default Homepage;
