export const API = {
    URL: `${import.meta.env.VITE_API_PROTOCOL}://${import.meta.env.VITE_API_URL}`,
    STORAGE: {
        RAT: "okp-rat",
        USER: "okp-user",
    },
    VERSION: import.meta.env.VITE_API_VERSION,
};

export const HTTP_METHODS = {
    GET: "GET",
    POST: "POST",
    PUT: "PUT",
    PATCH: "PATCH",
    DELETE: "DELETE",
};