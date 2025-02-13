export const ROUTER_CONFIG = {
  defaultLang: import.meta.env.VITE_LANG,
  supportedLangs: import.meta.env.VITE_LANGS.split(","),
  routeModules: import.meta.glob("/src/_services/routes/**/*.js", {
    eager: true,
  }),
  views: import.meta.glob("/src/pages/**/*.jsx", {
    eager: false,
  }),
  viewsPath: "/src/pages",
};
