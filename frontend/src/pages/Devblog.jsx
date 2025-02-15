import { t } from "@mcpronovost/okp-i18n";
import { switchLang } from "@mcpronovost/okp-router";

export default function Devblog() {
  
  const handleSwitchLang = (lang) => {
    window.location.href = switchLang(lang);
  };

  return (
    <div>
      <h1>Devblog</h1>
      <p>{t("Hello")}</p>
      <button onClick={() => handleSwitchLang("fr")}>FR</button>
      <button onClick={() => handleSwitchLang("en")}>EN</button>
    </div>
  );
}
