module.exports = {
    setupFilesAfterEnv: ["@testing-library/jest-dom/extend-expect"], // configurações para ser executado após o ambiente de teste ser configurado, adicionando asserções adicionais do jest-dom
    testEnvironment: "jest-environment-jsdom", // define o ambiente de teste para o jsdom, que simula um navegador para testes
    transform: {
      '^.+\\.jsx?$': 'babel-jest', // usa babel-jest para transformar arquivos JavaScript e JSX durante os testes
    },
    moduleNameMapper: {
      '\\.(css|scss)$': 'identity-obj-proxy', // mapeia arquivos CSS e SCSS para identity-obj-proxy para que possam ser usados nos testes sem erros
      '\\.(jpg|jpeg|png|gif|webp|svg)$': '<rootDir>/src/tests/__mocks__/fileMock.js', // mapeia arquivos de imagem para o mock de arquivo, permitindo o uso nos testes
    },
    moduleFileExtensions: ['js', 'jsx'], // define as extensões de arquivo a serem consideradas nos testes
    transformIgnorePatterns: [
      "node_modules/(?!react-leaflet|@react-leaflet|leaflet)"
    ],
  };
  