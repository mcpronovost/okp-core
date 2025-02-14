import "@/assets/style/main.scss";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { initI18n } from "@mcpronovost/okp-i18n";
import { initRouter } from "@mcpronovost/okp-router";
import { I18N_CONFIG } from "@/i18n/config";
import { ROUTER_CONFIG } from "@/router/config";
import App from "./App.jsx";

await initI18n(I18N_CONFIG);
await initRouter(ROUTER_CONFIG);

createRoot(document.getElementById("okp")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
