import React, { useState, useEffect } from "react";
import Table from "../../components/Table";
import { ContentContainer, PageContainer, TableTitle } from "./style";

const History = () => {
  const [history, setHistory] = useState([]); // Estado para armazenar o histórico de otimização

  // Hook useEffect para buscar o histórico ao carregar o componente
  useEffect(() => {
    fetchHistory();
  }, []);

  // Função assíncrona para buscar o histórico da API
  const fetchHistory = async () => {
    try {
      const response = await fetch("http://localhost:8000/results");
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setHistory(data); // Atualiza o estado com os dados recebidos
    } catch (error) {
      console.error("Error fetching history:", error);
    }
  };

  return (
    <PageContainer>
      <ContentContainer>
        <TableTitle>Optimization History</TableTitle>
        <Table data={history} /> {/* Renderiza a tabela com os dados do histórico */}
      </ContentContainer>
    </PageContainer>
  );
};

export default History;
