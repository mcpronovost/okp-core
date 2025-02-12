import { t } from "@mcpronovost/okp-i18n";
import { r } from "@mcpronovost/okp-router";

export default function Devblog() {
  const handleClick = (url) => {
    window.location.href = url;
  };

  return (
    <div>
      <h1>Devblog</h1>
      <p>{t("Hello")}</p>
      <button onClick={() => handleClick(r("devblog", "en", "fr"))}>FR</button>
      <button onClick={() => handleClick(r("devblog", "en", "en"))}>EN</button>
    </div>
  );
}
