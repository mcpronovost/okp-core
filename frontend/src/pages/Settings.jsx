import { r } from "@mcpronovost/okp-router";

export default function Settings() {
  return (
    <div>
      <h1>Settings</h1>
      <p>Welcome to the settings page</p>
      <a href={r("home")}>Go to Home</a>
    </div>
  );
}
