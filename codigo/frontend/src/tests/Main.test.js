import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";
import Main from "../pages/Main";

test('deve permitir a execução do cálculo com dados conhecidos', () => {
  render(
    <Router>
      <Main />
    </Router>
  );

  // simula a seleção do algoritmo
  fireEvent.change(screen.getByLabelText(/Selecione um algoritmo/i), { target: { value: 'greedy' } });
  
  // simula a inserção de valor no campo "Quantidade de dias de trabalho"
  fireEvent.change(screen.getByLabelText(/Quantidade de dias de trabalho/i), { target: { value: '5' } });
  
  // simula a inserção de valor no campo "Duração máxima do dia (em horas)"
  fireEvent.change(screen.getByLabelText(/Duração máxima do dia/i), { target: { value: '8' } });
  
  // simula a inserção de valor no campo "Velocidade do veículo (em km/h)"
  fireEvent.change(screen.getByLabelText(/Velocidade do veículo/i), { target: { value: '60' } });
  
  // simula a inserção de valor no campo "Tempo de início (em horas)"
  fireEvent.change(screen.getByLabelText(/Tempo de início/i), { target: { value: '8' } });
  
  // simula o clique no botão "Calcular"
  fireEvent.click(screen.getByText(/Calcular/i));

  // verifica se a mensagem de sucesso é exibida após o cálculo
  expect(screen.getByText(/As novas rotas foram calculadas com sucesso!/i)).toBeInTheDocument();
});
