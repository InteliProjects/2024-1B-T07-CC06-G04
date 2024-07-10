import axios from "axios";

export async function getTaskById(task_id) {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/results/${task_id}`
    );

    return response.data;
  } catch (error) {
    console.error("Error fetching results:", error);
  }
}
