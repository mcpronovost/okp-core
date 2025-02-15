/**
 * @see https://prettier.io/docs/en/configuration.html
 * @type {import("prettier").Config}
 */
const config = {
  semi: true,
  tabWidth: 2,
  printWidth: 79,
  trailingComma: "all",
  singleQuote: false,
  jsxSingleQuote: false,
  bracketSpacing: true,
  bracketSameLine: false,
  arrowParens: "always",
  endOfLine: "lf",
  plugins: ["prettier-plugin-css-order"],
  cssDeclarationSorterOrder: "smacss",
};

export default config;
