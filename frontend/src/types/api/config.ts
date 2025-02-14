export interface ApiStorageConfigType {
  rat: string;
  user: string;
}

export interface ApiConfigType {
  url: string;
  storage: ApiStorageConfigType;
  version: number;
  timeout: number;
  retryAttempts: number;
}

export type HttpMethodType = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
