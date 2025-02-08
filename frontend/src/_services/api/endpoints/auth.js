import { api } from "@/services/api";

/**
 * API client for authentication endpoints
 */
export const authApi = {
  login: (data) => api.post("/auth/login/", data),
  logout: () => api.post("/auth/logout/", null),
  logoutall: () => api.post("/auth/logoutall/", null),
  register: (data) => api.post("/auth/register/", data),
};

/**
 * EXAMPLE : Handle login
 */
export const handleLogin = async () => {
  const r = await authApi.login({
    username: "mc",
    password: "1",
  });
  if (r.status !== 200) {
    return console.warn(">> error : ", r.data);
  }
  console.log(">> response : ", r.data);
};

/**
 * EXAMPLE : Handle logout
 */
export const handleLogout = async () => {
  const r = await authApi.logout();
  if (r.status !== 204) {
    return console.warn(">> error : ", r.data);
  }
  console.log(">> response : ", r.data);
};

/**
 * EXAMPLE : Handle register
 */
export const handleRegister = async () => {
  const r = await authApi.register({
    username: "mc",
    password: "1",
  });
  if (r.status !== 201) {
    return console.warn(">> error : ", r.data);
  }
  console.log(">> response : ", r.data);
};
