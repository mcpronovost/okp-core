/**
 * I18N Configuration
 * 
 * Contains all I18N-related configuration including:
 * - Default language
 * - Supported languages
 * - Locales path
 * 
 * @example
 * import { I18N_CONFIG } from "@/configs/i18n.config";
 * const i18n = createI18n(I18N_CONFIG);
 */
export const I18N_CONFIG = {
  defaultLang: import.meta.env.VITE_LANG,
  supportedLangs: import.meta.env.VITE_LANGS.split(","),
  localesPath: "/src/_services/locales",
};
