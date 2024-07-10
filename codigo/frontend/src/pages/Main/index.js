import React, { useState, useEffect } from "react";
import { FiDownload, FiUpload, FiHelpCircle } from "react-icons/fi"; 
import { Link } from "react-router-dom";
import logo from "../../assets/logo-aegis.png";
import { PrimaryButton } from "../../components/Buttons/style";
import { useParams } from "react-router-dom";
import MapComponent from "../../components/Map/MapComponent";
import Modal from "../../components/Modal"; 

import {
  Container,
  DownloadButton,
  DownloadContainer,
  Header,
  LeftPanel,
  Map,
  Result,
  RightPanel,
  SuccessMessage,
  UploadContainer,
} from "./style";

const Main = () => {
  const { task_id } = useParams();
  const [markers, setMarkers] = useState([]);
  const [algorithm, setAlgorithm] = useState("");
  const [workDays, setWorkDays] = useState("");
  const [success, setSuccess] = useState(true);
  const [loading, setLoading] = useState(false);
  const [leiturists, setLeiturists] = useState("");
  const [file, setFile] = useState(null);
  const [taskID, setTaskID] = useState("");
  const [numAnts, setNumAnts] = useState(50);
  const [alpha, setAlpha] = useState(1);
  const [beta, setBeta] = useState(2);
  const [evaporationRate, setEvaporationRate] = useState(0.5);
  const [iterations, setIterations] = useState(100);

  // Estado para os modais
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalContent, setModalContent] = useState({ title: "", content: "" });

  const [routeIds, setRouteIds] = useState([]);
  const [selectedRouteId, setSelectedRouteId] = useState("");
  const [filteredMarkers, setFilteredMarkers] = useState([]);

  const openModal = (title, content) => {
    setModalContent({ title, content });
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  useEffect(() => {
    if (task_id) {
      fetchResults(task_id);
    }
  }, [task_id]);

// Pega o id do resultado e plota os marcadores de acordo
  const fetchResults = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/results/${id}`);
      const data = await response.json();

      var markers = [];

      var ids = []

      for (const i of Object.keys(data.results.results)) {
        ids.push(i);
        const result = data.results.results[i].best_tour[0];
        markers.push({"lat": result[0], "lon": result[1], "id": i});
      }

      setRouteIds(ids);
      setMarkers(markers)  
      setSuccess(true);

    } catch (error) {
      console.error("Error:", error);
    }
  };

  // Lida com o setup do arquivo csv de download
  const handleFileChange = (event) => {
    const newFile = event.target.files[0];
    setFile(newFile);
  };

  // Envia o csv dos dados para ser clusterizado
  const uploadCsv = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/upload-csv', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        alert("Erro no envio do CSV!")
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const url_cluster = new URL("http://localhost:8000/cluster-csv");
      url_cluster.searchParams.append("n_clusters_primary", workDays);
      url_cluster.searchParams.append("n_clusters_secondary", leiturists);

      const cluster = await fetch(url_cluster, {
        method: 'POST',
      })

      if (!cluster.ok) {
        throw new Error(`HTTP error! Status: ${cluster.status}`);
      }

    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  // Envia os dados do algoritmo para ser executado
  const handleCalculate = async () => {
    try {
      var response;
      if (algorithm === "antColony") {
              const url = new URL("http://localhost:8000/run-aco");
              url.searchParams.append("num_ants", numAnts);
              url.searchParams.append("alpha", alpha);
              url.searchParams.append("beta", beta);
              url.searchParams.append("evaporation_rate", evaporationRate);
              url.searchParams.append("iterations", iterations);

                response = await fetch(url, {
                method: "POST",
              });

      } else if (algorithm == "ortools") {
              response = await fetch("http://localhost:8000/api/run-ortools", {
              method: "POST",
            })
          } else {
            alert("Selecione um algoritmo!")
          }

          if (!response.ok) {
            alert("Preencha todos os campos necessários")
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          
      
          const data = await response.json();
          setTaskID(data.task_id);
          setSuccess(true);
          alert("A rota está sendo calculada. Em breve os resultados estarão prontos, você pode conferí-lo no histórico de execução.")
     } catch (error) {
    console.error("Error:", error);
    }
  };

  // Puxa os dados e chama a função para baixar o csv
  const handleDownload = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/results/${taskID}`);
      const data = await response.json();
      downloadCSV(data, `results_${taskID}`);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  // Converte o json dos resultados para csv
  const convertToCSV = (data) => {
    const { results } = data.results;
    const rows = [['Step', 'Best Tour Length', 'Best Tour']];

    for (const step in results) {
      const { best_tour_length, best_tour } = results[step];
      rows.push([step, best_tour_length, best_tour.join(' ')]);
    }

    let csvContent = "data:text/csv;charset=utf-8,";
    rows.forEach(rowArray => {
      let row = rowArray.join(",");
      csvContent += row + "\r\n";
    });

    return encodeURI(csvContent);
  };

  // Baixa o CSV com os dados dos resultados
  const downloadCSV = (data, fileTitle) => {
    const csv = convertToCSV(data);
    const link = document.createElement("a");
    link.setAttribute("href", csv);
    link.setAttribute("download", `${fileTitle}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  // Aplica o filtro baseado no ID da rota selecionada
  const applyFilter = () => {
    const filtered = selectedRouteId
      ? markers.filter(marker => marker.id === selectedRouteId)
      : markers;
    setFilteredMarkers(filtered);
  };

  // Renderiza os campos adicionais com base no algoritmo selecionado
  const renderAdditionalFields = () => {
    if (algorithm === "antColony") {
      return (
        <>
          <div>
            <label>Número de formigas
              <FiHelpCircle
                style={{ marginLeft: "8px", cursor: "pointer"}}
                onClick={() => openModal("Número de formigas", " Um número de formigas virtuais colocado aleatoriamente no grafo do problema a ser resolvido. Imagine que cada formiga faz sua busca sozinha usando as informações deixadas pelas formigas anteriores! Quanto mais formigas maior a probabilidade de encontrar um caminho melhor, mas isso pode aumentar muito o tempo de processamento!")}
              />
            </label>
            <input
              type="number"
              placeholder="10"
              value={numAnts}
              onChange={(e) => setNumAnts(e.target.value)}
            />
          </div>
          <div>
            <label>Alpha
              <FiHelpCircle
                style={{ marginLeft: "8px", cursor: "pointer" }}
                onClick={() => openModal("Alpha", "Define a influência do feromônio na escolha do caminho. Os feromônios são a forma pela qual as formigas se 'comunicam', caminhos com mais feromônios tem uma probabilidade maior de serem escolhidos. Aumentar esse valor significa fazer com que caminhos com mais feromônios sejam escolhidos mais rapidamente, o que pode diminuir a chance das formigas explorarem um caminho novo que poderia ser menor, entretanto, diminuir esse valor demais pode fazer com que elas demorem muito para convergirem em uma solução aceitável.")}
              />
            </label>
            <input
              type="number"
              placeholder="1.0"
              value={alpha}
              onChange={(e) => setAlpha(e.target.value)}
            />
          </div>
          <div>
            <label>Beta
              <FiHelpCircle
                style={{ marginLeft: "8px", cursor: "pointer" }}
                onClick={() => openModal("Beta", "Define a influência da heurística na escolha do caminho. A heurística de escolha do caminho pode ser interpretada como 'o quão visível esse caminho está?', se pensarmos na vida real, formigas são mais propensas a escolherem caminhos mais próximos por eles serem mais visíveis, portanto estão mais perto. Aumentar esse valor significa dar mais peso para caminhos mais próximos, o que parece ser bem lógico, mas lembre-se que caminhos inicialmente maiores podem resultar em uma rota menor à longo prazo.")}
              />
            </label>
            <input
              type="number"
              placeholder="2.0"
              value={beta}
              onChange={(e) => setBeta(e.target.value)}
            />
          </div>
          <div>
            <label>Taxa de evaporação
              <FiHelpCircle
                style={{ marginLeft: "8px", cursor: "pointer" }}
                onClick={() => openModal("Taxa de evaporação", "Define a taxa na qual o feromônio se evapora ao longo do tempo. Como explicado anteriormente, os feromônios influenciam imensamente na escolha das formigas, a ideia deles é que quanto maior o caminho, mais ele irá evaporar e menor será a chance de ser escolhido. Aumentar esse valor significa que os caminhos vão evaporar mais rápido, o que pode levar a um processamento de uma rota mais rápido, mas diminui a exploração das formigas que poderia levar a uma rota melhor. Em contrapartida, diminuir demais esse valor pode fazer com que leve muito tempo até que um caminho melhor seja escolhido.")}
              />
            </label>
            <input
              type="number"
              placeholder="0.5"
              value={evaporationRate}
              onChange={(e) => setEvaporationRate(e.target.value)}
            />
          </div>
          <div>
            <label>Iterações
              <FiHelpCircle
                style={{ marginLeft: "8px", cursor: "pointer" }}
                onClick={() => openModal("Iterações", "Define quantas vezes o processo de construção de soluções e atualização de feromônio será repetido. Mais iterações aumentam as chances das formigas encontrarem uma solução boa, mas também aumentam o tempo de processamento. Menos iterações processam mais rápido, mas podem resultar em caminhos pouco satisfatórios.")}
              />
            </label>
            <input
              type="number"
              value={iterations}
              placeholder="100"
              onChange={(e) => setIterations(e.target.value)}
            />
          </div>
        </>
      );
    }
    return null;
  };

  return (
    <div>
      <Header>
        <div className="logo-container">
          <img src={logo} alt="Logo Aegis" />
          <h2>Pangea</h2>
        </div>
        <Link
          to={"/history"}
          style={{ cursor: "pointer", textDecoration: "none", color: "#fff" }}
        >
          <h2>Histórico de Execução</h2>
        </Link>
      </Header>
      <Container>
        <LeftPanel>
          <h2>Faça o upload de um arquivo CSV</h2>
          <UploadContainer>
            <label style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
              <FiUpload size={24} style={{ marginBottom: "8px" }} />
              <p>{file ? file.name : "Faça o upload de um CSV"}</p>
              <input
                type="file"
                accept=".csv"
                onChange={handleFileChange}
                style={{ display: "none" }}
              />
            </label>
          </UploadContainer>

          <div>
            <label>Quantidade de leituristas</label>
            <input
              type="number"
              value={leiturists}
              onChange={(e) => setLeiturists(e.target.value)}
            />
          </div>
          <div>
            <label>Quantidade de dias de trabalho</label>
            <input
              type="number"
              value={workDays}
              onChange={(e) => setWorkDays(e.target.value)}
            />
          </div>
          {file ? (
            <>
              {loading ? (
                <p>Carregando o CSV, espere um momento...</p>
              ) : (
                <PrimaryButton onClick={() => uploadCsv(file)}>Carregar CSV</PrimaryButton>
              )}
            </>
          ) : null}

          <h2>Selecione um algoritmo para executar
          <FiHelpCircle
                style={{ marginLeft: "8px", cursor: "pointer"}}
                onClick={() => openModal("Algoritmos", " *OR Tools*: Conjunto de bibliotecas de software de código aberto desenvolvido pela Google para resolver problemas de otimização combinatória, como roteirização de veículos, planejamento de produção, agendamento e problemas de satisfatibilidade. *Ant Colony*: Algoritmo de otimização baseado no comportamento de formigas, que buscam o caminho mais curto entre o formigueiro e a fonte de alimento. Dica: Caso queira testar os parâmetros de Alpha e Beta use um número fixo de formigas, um número neutro de taxa de evaporação (ex: 0.5) e um número de iterações baixo, foque em estudar como os dois parâmetros afetam a solução, quando encontrar uma combinação que maximize os resultados que deseja para esses dois parâmetros, aumente o número de iterações e formigas para garantir resultados mais estáveis. Ao final, modifique a taxa de evaporação com valores que vão diminuindo gradualmente até que entenda se é melhor aumentá-la ou diminuí-la, quando encontrar o melhor valor, faça mudanças mais pontuais seguindo a mesma lógica, repita esse processo até encontrar valores satisfatórios.")}
              />
          </h2>
          <select
            value={algorithm}
            onChange={(e) => {
              setAlgorithm(e.target.value);
              setNumAnts("");
              setAlpha("");
              setBeta("");
              setEvaporationRate("");
              setIterations("");
            }}
          >
            <option value="1">Selecione um algoritmo</option>
            <option value="ortools">OR Tools</option>
            <option value="antColony">Ant Colony</option>
          </select>
          {renderAdditionalFields()}
          {file && (
            <PrimaryButton onClick={handleCalculate}>Calcular</PrimaryButton>
          )}
        </LeftPanel>
        <RightPanel>
          {success && (
            <>
        <Map>
          {/* Add a filter dropdown for route IDs */}
          <div style={{ marginBottom: '10px' }}>
            <label htmlFor="routeFilter">Filtrar pelo ID da rota: </label>
            <select
              id="routeFilter"
              value={selectedRouteId}
              onChange={(e) => setSelectedRouteId(e.target.value)}
            >
              <option value="">Exibir todos</option>
              {routeIds.map(routeId => (
                <option key={routeId} value={routeId}>
                  {routeId}
                </option>
              ))}
            </select>
            <PrimaryButton onClick={applyFilter} style={{ marginLeft: '10px' }}>Filtrar</PrimaryButton>
          </div>
          <MapComponent markers={filteredMarkers} />
        </Map>
              <Result>
                <SuccessMessage>
                  <h3>Sucesso</h3>
                  <br></br>
                  <p>As novas rotas foram calculadas com sucesso!</p>
                  <br></br>
                  <p>
                    Observe o resultado no mapa acima ou faça o download do CSV
                    ao lado.
                  </p>
                </SuccessMessage>
                <DownloadContainer>
                  <DownloadButton onClick={handleDownload}>
                    <FiDownload />
                  </DownloadButton>
                  <p>Baixar roteirização</p>
                </DownloadContainer>
              </Result>
            </>
          )}
        </RightPanel>
      </Container>
      {isModalOpen && (
        <Modal title={modalContent.title} content={modalContent.content} onClose={closeModal} />
      )}
    </div>
  );
};

export default Main;
