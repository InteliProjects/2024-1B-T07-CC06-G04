import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import History from '../pages/HistoryPage';

// teste que verifica se a página History carrega corretamente
test('deve carregar a página History corretamente', () => {
  render(
    <Router>
      <History />
    </Router>
  );
  expect(screen.getByText(/Optimization History/i)).toBeInTheDocument(); // verifica se o texto "Optimization History" está presente na página
});
