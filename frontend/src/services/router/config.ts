import type { RouterConfigType } from "@/types";

export const ROUTER_CONFIG: RouterConfigType = {
  defaultLang: import.meta.env.VITE_LANG,
  supportedLangs: import.meta.env.VITE_LANGS.split(","),
  routeModules: import.meta.glob("/src/services/router/routes/**/*.js", {
    eager: true,
  }),
  views: import.meta.glob("/src/pages/**/*.jsx", {
    eager: false,
  }),
  viewsPath: "/src/pages",
};
