import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base: "/",
  server: {
    host: "localhost",
    port: 5173,
    origin: "http://localhost:5173",
    proxy: {
      "/api": "http://127.0.0.1:8000",
    },
  },
  build: {
    assetsDir: "",
    rollupOptions: {
      output: {
        entryFileNames: "static/js/[name]-[hash].js",
        chunkFileNames: "static/js/[name]-[hash].js",
        assetFileNames: "static/[ext]/[name]-[hash].[ext]",
      },
    },
  },
});
