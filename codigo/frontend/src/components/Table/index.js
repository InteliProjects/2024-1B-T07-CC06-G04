import React from "react";
import { Link } from "react-router-dom";
import { PrimaryButton } from "../Buttons/style";
import {
  TableCell,
  TableContainer,
  TableElement,
  TableHeader,
  TableRow,
} from "./style";

function Table({ data }) {
  return (
    <TableContainer>
      <TableElement>
        <thead>
          <tr>
            <TableHeader>Status</TableHeader>
            <TableHeader>Algoritmo</TableHeader>
            <TableHeader>Data</TableHeader>
            <TableHeader>Resultados</TableHeader>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <TableRow key={item.task_id}>
              <TableCell>{item.status}</TableCell>
              <TableCell>{item.data.algorithm}</TableCell>
              <TableCell>{item.data.datetime}</TableCell>
              <TableCell>
                <Link to={`/main/${item.task_id}`}>
                  <PrimaryButton>Visualizar</PrimaryButton>
                </Link>
              </TableCell>
            </TableRow>
          ))}
        </tbody>
      </TableElement>
    </TableContainer>
  );
}

export default Table;
