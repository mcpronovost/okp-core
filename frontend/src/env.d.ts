/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_LANG: string;
  readonly VITE_LANGS: string;
  readonly VITE_TZ: string;
  readonly VITE_API_PROTOCOL: string;
  readonly VITE_API: string;
  readonly VITE_API_VERSION: number;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
