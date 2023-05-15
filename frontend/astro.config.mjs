import { defineConfig } from "astro/config";
import node from "@astrojs/node";
import react from "@astrojs/react";

// https://astro.build/config
export default defineConfig({
  output: "server",
  server: {
    port: 3000
  },
  adapter: node({
    mode: "standalone"
  }),
  experimental: {
    middleware: true
  },
  integrations: [
    react()
  ],
  vite: {
    define: {
      "__REACT_DEVTOOLS_GLOBAL_HOOK__": "({ isDisabled: true })"
    }
  }
});