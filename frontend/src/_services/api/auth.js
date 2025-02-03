import { api } from "@/services/api";

export const authApi = {
  login: (data) => api.post("/auth/login/", data),
  logout: () => api.post("/auth/logout/", null),
  logoutall: () => api.post("/auth/logoutall/", null),
  register: (data) => api.post("/auth/register/", data),
};

// Example login usage
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

// Example logout usage
export const handleLogout = async () => {
  const r = await authApi.logout();
  if (r.status !== 204) {
    return console.warn(">> error : ", r.data);
  }
  console.log(">> response : ", r.data);
};

// Example register usage
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
