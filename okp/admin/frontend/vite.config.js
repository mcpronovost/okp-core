import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import path from "path"

export default defineConfig({
  plugins: [vue()],
  base: process.env.NODE_ENV === "production" ? "/static/okp-admin/" : "/",
  server: {
    host: "localhost",
    port: 5173,
    strictPort: true,
    origin: "http://localhost:5173",
  },
  build: {
    outDir: "../static/okp-admin",
    emptyOutDir: true,
    rollupOptions: {
      output: {
        assetFileNames: (assetInfo) => {
          let extType = assetInfo.name.split(".")[1]
          if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(extType)) {
            extType = "img"
          }
          return `assets/${extType}/[name][extname]`
        },
        chunkFileNames: "assets/js/[name].js",
        entryFileNames: "assets/js/[name].js",
      },
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})