import axios from "axios";
import { API_URL } from "../constants/ApiURL";

export function uploadCsv(csv) {
  console.log(csv);
  const form = new FormData();
  form.append("file", csv);

  const config = {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "multipart/form-data",
    },
  };

  axios
    .post(`${API_URL}/upload-csv`, form, config)
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.error("Erro: ", error);
    });
}
