export interface RouteModuleType {
  [key: string]: any;
}

export interface ViewComponentType {
  [key: string]: any;
}

export interface RouterConfigType {
  defaultLang: string;
  supportedLangs: string[];
  routeModules: Record<string, RouteModuleType>;
  views: Record<string, () => Promise<ViewComponentType>>;
  viewsPath: string;
}
