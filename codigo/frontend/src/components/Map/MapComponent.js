import React from "react";
import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

// Corrigindo o problema do ícone padrão do leaflet
delete L.Icon.Default.prototype._getIconUrl;

// Definindo as opções padrão do ícone
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

// Função para criar um ícone personalizado com um número
const createCustomIcon = (index) => {
  return L.divIcon({
    html: `<div style="background-color: #FF0000; color: white; border-radius: 50%; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; font-size: 12px;">${index + 1}</div>`,
    className: '',
    iconSize: [24, 24],
  });
};

// Definindo o componente MapComponent
const MapComponent = ({ markers, filterRouteId }) => {
  // Filtrar os marcadores com base no ID da rota selecionada
  const filteredMarkers = filterRouteId
    ? markers.filter(marker => marker.id === filterRouteId)
    : markers;

  // Extract positions for the Polyline
  const positions = filteredMarkers.map(marker => [marker.lat, marker.lon]);

  return (
    // Definindo o container do mapa com o centro e o nível de zoom iniciais
    <MapContainer center={[-22.9618, -43.2037]} zoom={13} style={{ width: "100%", height: "100%" }}>
      {/* Adicionando a camada de tiles ao mapa */}
      <TileLayer
        // Atribuindo créditos ao OpenStreetMap
        attribution='© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        // Definindo a URL dos tiles
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {/* Adicionando a linha que conecta os marcadores */}
      <Polyline positions={positions} color="blue" />
      {/* Iterando sobre os marcadores filtrados e adicionando-os ao mapa */}
      {filteredMarkers.map((marker, idx) => (
        // Definindo a posição de cada marcador com um ícone personalizado
        <Marker
          key={idx}
          position={[marker.lat, marker.lon]}
          icon={createCustomIcon(idx)}
        >
          {/* Adicionando um popup a cada marcador */}
          <Popup>
            Route Code: {marker.id}<br />
            Marker {idx + 1}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

// Exportando o componente MapComponent como padrão
export default MapComponent;
