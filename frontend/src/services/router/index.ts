import { useEffect, useState, useCallback } from "react";
import { getView, r } from "@mcpronovost/okp-router";

interface RouterState {
  View: React.ComponentType<any> | null;
  props: Record<string, any>;
  params: Record<string, string> | null;
  isLoading: boolean;
}

export function useRouter() {
  const [state, setState] = useState<RouterState>({
    View: null,
    props: {},
    params: null,
    isLoading: true,
  });

  const loadView = useCallback(async () => {
    setState((prev) => ({ ...prev, isLoading: true }));

    try {
      const { viewModule, props, params } = await getView();

      setState({
        View: viewModule.default,
        props: props || {},
        params: params || null,
        isLoading: false,
      });
    } catch (error) {
      console.error("Failed to load view:", error);
      setState((prev) => ({ ...prev, isLoading: false }));
    }
  }, []);

  const navigate = useCallback(
    (
      uri: string,
      langTo?: string,
      langFrom?: string,
      params?: Record<string, string>
    ) => {
      const path = r(uri, langTo, langFrom, params);
      window.history.pushState({}, "", path);
      loadView();
    },
    [r, loadView]
  );

  useEffect(() => {
    loadView();

    // Handle browser back/forward buttons
    const handlePopState = () => {
      loadView();
    };

    window.addEventListener("popstate", handlePopState);
    return () => window.removeEventListener("popstate", handlePopState);
  }, [loadView]);

  return {
    View: state.View,
    props: state.props,
    params: state.params,
    isLoading: state.isLoading,
    navigate,
    n: navigate,
  };
}

export default useRouter;
