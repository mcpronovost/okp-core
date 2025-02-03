import { LANG_DEFAULT } from "@/services/utils/constants";
// import { routesAuth } from "./routes/auth";
// import { routesManagement } from "./routes/management";

/**
 * Global Routes
 */
export const routes = {
  home: {
    view: "Home",
    paths: {
      en: "",
      fr: "",
    },
  },
  devblog: {
    view: "Devblog",
    paths: {
      en: "devblog",
      fr: "devblog",
    },
  },
  faq: {
    view: "FAQ",
    paths: {
      en: "faq",
      fr: "faq",
    },
  },
  // ...routesAuth,
  // ...routesManagement,
  settings: {
    view: "Settings",
    paths: {
      en: "settings",
      fr: "parametres",
    },
  },
};

/**
 * Recursively finds a route by matching the URI to translations in the route map
 * @param uri - The URI path to match against route translations
 * @param lang - The language code to use for matching (e.g., "en" or "fr")
 * @param routesList - Optional route map to search through. Defaults to global routes if not provided
 * @param parentPath - Optional dot-notation path of parent routes. Used internally for recursion
 * @returns A tuple containing [fullRoutePath, routeObject] if found, undefined otherwise
 */
export const findRoute = (uri, lang, routesList, parentPath = "") => {
  if (!routesList) routesList = routes;
  const params = {};

  for (const [key, route] of Object.entries(routesList)) {
    const fullPath = parentPath ? `${parentPath}.${key}` : key;
    const routePath = route.paths[lang];

    // Handle dynamic path segments
    if (routePath.includes("{")) {
      // Extract parameter names from the route path
      const paramNames = [...routePath.matchAll(/{([^}]+)}/g)].map(
        (match) => match[1]
      );
      const pathPattern = routePath.replace(/{[^}]+}/g, "([^/]+)");
      const regex = new RegExp(`^${pathPattern}$`);
      const matches = uri.match(regex);

      if (matches) {
        // Store captured values with their parameter names
        paramNames.forEach((name, index) => {
          params[name] = matches[index + 1];
        });
        return [fullPath, { ...route, params }];
      }
    } else if (routePath === uri) {
      return [fullPath, { ...route, params }];
    }

    // Check for child routes recursively
    if (route.children) {
      const childUri = `${route.paths[lang]}/`;
      if (
        uri.startsWith(childUri) ||
        (routePath.includes("{") &&
          new RegExp(`^${routePath.replace(/{[^}]+}/g, "[^/]+")}/`).test(uri))
      ) {
        const nextParentPath = parentPath ? `${parentPath}.${key}` : key;

        // Extract params from current level if it's a dynamic route
        if (routePath.includes("{")) {
          const paramNames = [...routePath.matchAll(/{([^}]+)}/g)].map(
            (match) => match[1]
          );
          const pathPattern = routePath.replace(/{[^}]+}/g, "([^/]+)");
          const matches = uri.match(new RegExp(`^${pathPattern}/`));
          if (matches) {
            paramNames.forEach((name, index) => {
              params[name] = matches[index + 1];
            });
          }
        }

        const childRoute = findRoute(
          uri.replace(
            new RegExp(`^${routePath.replace(/{[^}]+}/g, "[^/]+")}/`),
            ""
          ),
          lang,
          route.children,
          nextParentPath
        );

        if (childRoute) {
          // Merge params from child route with current params
          return [childRoute[0], childRoute[1]];
        }
      }
    }
  }
  return [
    uri,
    {
      view: "common/NotFound",
      auth: false,
      props: {},
      params: {},
    },
  ];
};

/**
 * Translates a route URI from one language to another
 * @param uri - The current URI path
 * @param fromLang - The language code of the current URI
 * @param toLang - The target language code to translate the URI to
 * @returns The translated URI path in the new language, or the original URI if no translation is found
 */
export const findLocaleRoute = (uri, fromLang, toLang, additionalParams) => {
  // Find the current route based on the URI and current language
  const currentRoute = findRoute(uri, fromLang);
  if (!currentRoute) return `/${toLang}/${uri}`;

  const [routePath, routeData] = currentRoute;
  const params = { ...routeData.params, ...additionalParams };

  // Split the route path to handle nested routes
  const routeParts = routePath.split(".");
  let routesList = routes;
  let toPath = "";

  // Build the new path by traversing the route tree
  for (let i = 0; i < routeParts.length; i++) {
    const part = routeParts[i];
    const currentPart = routesList[part];

    if (currentPart) {
      toPath += (i > 0 ? "/" : "") + currentPart.paths[toLang];
      routesList = currentPart.children || {};
    }
  }

  // Replace params in the path
  if (params) {
    for (const [key, value] of Object.entries(params)) {
      toPath = toPath.replace(`{${key}}`, value);
    }
  }

  return `/${toLang}/${toPath}`;
};

export const getRoute = (toLang = LANG_DEFAULT) => {
  return {
    r: (uri, params) => findLocaleRoute(uri, "en", toLang, params),
  };
};
