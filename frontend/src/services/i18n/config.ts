import type { I18nConfigType } from "@mcpronovost/okp-i18n";

export const I18N_CONFIG: I18nConfigType = {
  defaultLang: import.meta.env.VITE_LANG,
  supportedLangs: import.meta.env.VITE_LANGS.split(","),
  localesPath: "/src/services/i18n/locales",
};
