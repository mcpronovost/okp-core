import { useRouter } from "@/services/router";
import Loading from "@/pages/Loading";
import Error404 from "@/pages/errors/404";

export default function App() {
  const { View, props, params, isLoading } = useRouter();

  if (isLoading) {
    return <Loading />;
  }

  if (!View) {
    return <Error404 />;
  }

  return <View {...props} {...params} />;
}
