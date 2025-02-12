import { t } from "@mcpronovost/okp-i18n";
import { r } from "@mcpronovost/okp-router";

export default function Home() {
  return (
    <div>
      <h1>Home</h1>
      <p>{t("Hello")}</p>
      <a href={r("home", "en", "fr")}>Go to Home FR</a>
      <a href={r("home", "en", "en")}>Go to Home EN</a>
    </div>
  );
}
