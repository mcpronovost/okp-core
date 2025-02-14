import { t } from "@mcpronovost/okp-i18n";
import { useRouter } from "@/services/router";

export default function Home() {
  const { n } = useRouter();

  return (
    <div>
      <h1>Home</h1>
      <p>{t("Hello")}</p>
      <button onClick={() => n("home", "fr")}>Go to Home FR</button>
      <button onClick={() => n("home", "en")}>Go to Home EN</button>
    </div>
  );
}
