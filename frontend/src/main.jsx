import "@/assets/style/main.scss";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { initRouter } from "@mcpronovost/okp-router";
import App from "./App.jsx";

initRouter({
  defaultLang: import.meta.env.VITE_LANG,
  supportedLangs: import.meta.env.VITE_LANGS.split(","),
  routeModules: import.meta.glob("./_services/routes/**/*.js", {
    eager: true,
  }),
  views: import.meta.glob("./views/**/*.jsx", {
    eager: false,
  })
});

createRoot(document.getElementById("okp")).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
