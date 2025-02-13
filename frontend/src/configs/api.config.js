export const API_CONFIG = {
  development: {
    url: `${import.meta.env.VITE_API_PROTOCOL}://${
      import.meta.env.VITE_API_URL
    }`,
    storage: {
      rat: "okp-rat",
      user: "okp-user",
    },
    version: import.meta.env.VITE_API_VERSION,
    timeout: 5000,
    retryAttempts: 3,
  },
  production: {
    url: `https://${import.meta.env.VITE_API_URL}`,
    storage: {
      rat: "okp-rat",
      user: "okp-user",
    },
    version: import.meta.env.VITE_API_VERSION,
    timeout: 5000,
    retryAttempts: 3,
  },
}[import.meta.env.MODE];

export const HTTP_METHODS = {
  GET: "GET",
  POST: "POST",
  PUT: "PUT",
  PATCH: "PATCH",
  DELETE: "DELETE",
};
