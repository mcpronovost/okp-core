import { t } from "@mcpronovost/okp-i18n";
import { switchLang } from "@mcpronovost/okp-router";
import OkpAlert from "@/components/feedback/Alert";

export default function Devblog() {
  
  const handleSwitchLang = (lang) => {
    window.location.href = switchLang(lang);
  };

  const handleCloseAlert = () => {
    console.log("close");
  };

  return (
    <div style={{ width: "100%", maxWidth: "1000px", margin: "0 auto" }}>
      <h1>Devblog</h1>
      <p>{t("Hello")}</p>
      <button onClick={() => handleSwitchLang("fr")}>FR</button>
      <button onClick={() => handleSwitchLang("en")}>EN</button>
      <div style={{ margin: "24px" }}>
        <OkpAlert />
      </div>
      <div style={{ margin: "24px" }}>
        <OkpAlert>This is a default alert</OkpAlert>
      </div>
      <div style={{ margin: "24px" }}>
        <OkpAlert title="This is my title" icon={false} closable onClose={handleCloseAlert}>
          This is a default alert without icon
        </OkpAlert>
      </div>
      <div style={{ margin: "24px" }}>
        <OkpAlert title="Profile updated" variant="success">Your profile has been updated successfully.</OkpAlert>
      </div>
      <div style={{ margin: "24px" }}>
        <OkpAlert title="An error occurred" message="Your profile could not be updated." variant="error">Please, try again later.</OkpAlert>
      </div>
      <div style={{ margin: "24px" }}>
        <OkpAlert variant="warning" title="This is a warning alert" />
      </div>
      <div style={{ margin: "24px" }}>
        <OkpAlert variant="info">This is an info alert</OkpAlert>
      </div>
    </div>
  );
}
