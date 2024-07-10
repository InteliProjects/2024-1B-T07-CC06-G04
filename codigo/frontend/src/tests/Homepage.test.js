import React from 'react'; // importa o React
import { render, screen, fireEvent } from '@testing-library/react'; // importa funções de teste do @testing-library/react
import { BrowserRouter as Router } from 'react-router-dom'; // importa o Router para simular a navegação
import Homepage from '../pages/Homepage'; // importa o componente Homepage

// Teste para carregar a Homepage corretamente
test('deve carregar a Homepage corretamente', () => {
  render(
    <Router>
      <Homepage />
    </Router>
  );
  // verifica se o texto "Faça o upload de um CSV" está presente na página
  expect(screen.getByText(/Faça o upload de um CSV/i)).toBeInTheDocument();
});

// Teste para permitir o upload de um arquivo CSV
test('deve permitir o upload de um arquivo CSV', () => {
  render(
    <Router>
      <Homepage />
    </Router>
  );
  // seleciona o input de arquivo pelo rótulo de acessibilidade
  const fileInput = screen.getByLabelText(/Faça o upload de um CSV/i);
  // cria um arquivo fictício para simular o upload
  const file = new File(['file contents'], 'example.csv', { type: 'text/csv' });

  // dispara o evento de mudança no input de arquivo, simulando o upload
  fireEvent.change(fileInput, { target: { files: [file] } });
  // verifica se o nome do arquivo aparece na página após o upload
  expect(screen.getByText('example.csv')).toBeInTheDocument();
});
