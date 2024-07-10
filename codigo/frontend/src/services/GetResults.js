import axios from "axios";

export async function fetchHistory() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/results");
    return response.data;
  } catch (error) {
    console.error("Error fetching history:", error);
  }
}
