import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

// https://vite.dev/config/
export default ({ mode }) => {
  const rootPath = path.resolve(__dirname, "..");
  const env = loadEnv(mode, rootPath, "");
  process.env = {...process.env, ...env};
  return defineConfig({
    plugins: [react()],
    base: "/",
    server: {
      host: "localhost",
      port: 5173,
      origin: "http://localhost:5173",
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
    resolve: {
      alias: {
        "@/assets": "/src/_assets",
        "@/services": "/src/_services",
        "@": "/src",
      },
    },
  });
};
