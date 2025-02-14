import axios from "axios";
import { API_CONFIG } from "@/configs";
import { HTTP_METHODS } from "@/services/utils/constants";

const getCookie = (name) => document.cookie?.match(`${name}=([^;]+)`)?.[1];

/**
 * Default headers for API requests
 */
const defaultHeaders = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Accept-CH": "Sec-CH-UA-Platform",
  "x-okp-api-version": API_CONFIG.version,
};

/**
 * Axios instance configured for client-side API requests
 */
export const doAxios = axios.create({
  baseURL: `${API_CONFIG.url}/v${API_CONFIG.version}/`,
  withCredentials: true,
  headers: defaultHeaders,
});

/**
 * Adds authorization header to request if token exists
 * @param headers - Current request headers
 * @param token - Authorization token
 * @returns Updated headers with authorization
 */
const addAuthorizationHeader = (headers) => {
  headers["Accept-Language"] = window?.document?.documentElement?.lang || globalThis.currentLang;

  // Add authorization token if exists
  const authToken = getCookie(API_CONFIG.storage.rat);
  if (authToken) headers.Authorization = `OKP ${authToken}`;
  
  // Add CSRF token if exists
  const csrfToken = getCookie("csrftoken");
  if (csrfToken) headers["X-CSRFToken"] = csrfToken;
  return headers;
};

/**
 * Processes request errors and formats them consistently
 * @param response - The error response from the request
 * @returns Stringified error object with status and message
 */
const doRequestError = async (response) => {
  const defaultMsg = "An error occurred";
  if (!response) return { status: 0, msg: defaultMsg };

  const { status, data } = response;
  const errorMap = {
    "ERR_BAD_REQUEST": () => data || defaultMsg,
    400: () => data || defaultMsg,
    401: () =>
      data?.detail?.includes("Token")
        ? "Unauthorized access"
        : data?.detail || defaultMsg,
    403: () => data || defaultMsg,
  };

  return {
    status: status || 0,
    msg: errorMap[status]?.() || defaultMsg,
  };
};

// Request interceptor
// This interceptor adds the Authorization header with the token if it exists
doAxios.interceptors.request.use((config) => {
  config.headers = addAuthorizationHeader(config.headers);
  return config;
});

// Response interceptor
// This interceptor processes responses and handles specific error cases
doAxios.interceptors.response.use(
  (response) => response,
  async (error) => Promise.reject(await doRequestError(error.response || {
    status: error.code,
    data: error.message,
  } || error))
);

/**
 * Universal request handler that works both client and server side
 * Uses Axios for client-side requests and fetch for server-side
 * @param method - HTTP method to use
 * @param url - API endpoint URL
 * @param data - Request payload (optional)
 * @param options - Additional request options
 * @returns Promise resolving to AxiosResponse, Response, or Error
 */
const doRequest = async (method, url, data, options = {}) => {
  try {
    return await doAxios.request({ url, method, data, ...options });
  } catch (error) {
    throw error instanceof Error ? error.message : error;
  }
};

/**
 * API client with methods for common HTTP operations
 * Perform GET request
 * @param url - API endpoint URL
 * @param options - Request options
 */
export const api = Object.fromEntries(
  Object.entries(HTTP_METHODS).map(([key, method]) => [
    key.toLowerCase(),
    (url, data, options = {}) => doRequest(method, url, data, options),
  ])
);

export { authApi } from "./endpoints/auth";
