import { useEffect, useState } from "react";
import { getView } from "@mcpronovost/okp-router";
import Loading from "@/pages/Loading";

function App() {
  const [OkpView, setOkpView] = useState(null);
  const [viewProps, setViewProps] = useState({});
  const [viewParams, setViewParams] = useState({});

  const doSetView = async () => {
    const { viewModule, props, params } = await getView();

    setViewProps(props || {});
    setViewParams(params || {});

    setOkpView(() => viewModule.default);
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
