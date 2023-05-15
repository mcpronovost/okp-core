import axios from "axios";
import { getCookie } from "@/scripts/utils/generics";

const csrftoken = getCookie("csrftoken");

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    Accepted: "application/json",
    "Content-Type": "application/json",
    "X-CSRFToken": csrftoken
  },
});

export default axiosInstance;
