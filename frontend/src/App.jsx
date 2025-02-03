import { useEffect, useState } from "react";
import { findRoute } from "@/services/router";
import Loading from "@/views/Loading";

function App() {
  const lang = document.documentElement.lang;
  const uri = window.location.pathname.replace(/^\/[a-z]{2}\//, "");
  const [OkpView, setOkpView] = useState(null);
  const [viewProps, setViewProps] = useState({});
  const [viewParams, setViewParams] = useState({});

  const doSetView = async () => {
    /**
     * Find the route by matching the URI to translations
     */
    const route = findRoute(uri, lang);

    /**
     * Redirect to 404 if no route is found
     */
    if (!route) {
      return window.location.href = `/${lang}/404`;
    }

    try {
      /**
       * Get the view component
       */
      const [_, { view, auth, props, params }] = route;
      const viewModule = await import(`./views/${view}.jsx`);
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
