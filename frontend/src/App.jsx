import { useEffect, useState } from "react";
import { findRoute } from "@/services/router";
import { LANGUAGES } from "@/services/utils/constants";
import Loading from "@/views/Loading";

const views = import.meta.glob("./views/**/*.jsx", {
    eager: false,
});

function App() {
  const lang = document.documentElement.lang;
  const path = window.location.pathname
  const [, langCode, ...uriParts] = path.split(/^\/([a-z]{2})\//);
  const uri = uriParts.join("/");

  // If the language is not supported, redirect to the default language
  if (!langCode || !LANGUAGES.includes(langCode)) {
    window.location.href = `/${lang}/${uri || path.replace(/^\//, "")}`;
  }

  const [OkpView, setOkpView] = useState(null);
  const [viewProps, setViewProps] = useState({});
  const [viewParams, setViewParams] = useState({});

  const doSetView = async () => {
    const route = findRoute(uri, lang);

    if (!route) {
      // If the route is not found, redirect to the 404 page
      return window.location.href = `/${lang}/404`;
    }

    try {
      const [_, { view, auth, props, params }] = route;
      const viewPath = `./views/${view}.jsx`;

      if (!views[viewPath]) {
        // If the view is not found, redirect to the 404 page
        return window.location.href = `/${lang}/404`;
      }

      const viewModule = await views[viewPath]();

      /**
       * Set the view props and params
       */
      setViewProps(props || {});
      setViewParams(params || {});

      /**
       * Get the user data
       */
      // const me = await usersApi.me();

      /**
       * Redirect to 403 if the route is protected and the user is not authenticated
       */
      // if (auth && !me) {
      //   return Astro.redirect(`/${lang}/403`);
      // }

      /**
       * Set the view component
       */
      setOkpView(() => viewModule.default);
    } catch (error) {
      console.error("Failed to load view:", error);
      // window.location.href = `/${lang}/404`;
    }
  };

  useEffect(() => {
    doSetView();
  }, []);

  if (OkpView) {
    return <OkpView {...viewProps} {...viewParams} />;
  }

  return <Loading />;
}

export default App;
