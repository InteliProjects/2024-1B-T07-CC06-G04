import React from "react";
import { LeftMapContainer } from "./style";
import { MapContainer } from "react-leaflet/MapContainer";
import { TileLayer } from "react-leaflet/TileLayer";
import { Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

function Map() {
  // var CartoDB_Voyager = L.tileLayer(
  //   "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
  //   {
  //     attribution:
  //       '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  //     subdomains: "abcd",
  //     maxZoom: 20,
  //   }
  // );

  // var Esri_WorldImagery = L.tileLayer(
  //   "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
  //   {
  //     attribution:
  //       "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
  //   }
  // );

  // var CartoDB_Positron = L.tileLayer(
  //   "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
  //   {
  //     attribution:
  //       '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  //     subdomains: "abcd",
  //     maxZoom: 20,
  //   }
  // );

  // var CartoDB_Voyager = L.tileLayer(
  //   "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
  //   {
  //     attribution:
  //       '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  //     subdomains: "abcd",
  //     maxZoom: 20,
  //   }
  // );

  return (
    <LeftMapContainer>
      <MapContainer
        style={{ width: "80%", height: "100vh", marginLeft: "20%" }}
        center={[-22.9618, -43.2037]}
        zoom={13}
        scrollWheelZoom={false}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
        />
        <Marker position={[51.505, -0.09]}></Marker>
      </MapContainer>
    </LeftMapContainer>
  );
}

export default Map;
