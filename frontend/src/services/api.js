import axios from "axios";

const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_BASE_URL
    || "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 600000,
});

export async function searchCandidates(
  jobDescription,
) {
  const response = await api.post(
    "/search-candidates",
    {
      job_description: jobDescription,
    },
  );

  return response.data;
}

export default api;
