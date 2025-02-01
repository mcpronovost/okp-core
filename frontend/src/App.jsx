import { useState } from "react";
import axios from "axios";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/react.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);
  const [token, setToken] = useState(null);

  const handleLogin = () => {
    axios
      .post(
        "http://localhost:8000/api/v1/auth/login/",
        {
          username: "mc",
          password: "1",
        },
        {
          headers: {
            "Accept-CH": "Sec-CH-UA-Platform",
          },
        }
      )
      .then((response) => {
        if (response.status !== 200) {
          throw new Error({
            message: "Login failed",
            status: response.status,
          });
        }
        setToken(response.data.token);
      })
      .catch((e) => {
        console.log(">> error : ", e.response.data);
      });
  };

  const handleLogout = () => {
    axios
      .post("http://localhost:8000/api/v1/auth/logout/", null, {
        headers: {
          Authorization: `okp ${token}`,
        },
      })
      .then((response) => {
        if (response.status !== 204) {
          throw new Error({
            message: "Logout failed",
            status: response.status,
          });
        }
        setToken(null);
      })
      .catch((e) => {
        console.log(">> error : ", e.response.data);
      });
  };

  const handleRegister = () => {
    axios
      .post(
        "http://localhost:8000/api/v1/auth/register/",
        {},
        {
          headers: {
            "Accept-CH": "Sec-CH-UA-Platform",
          },
        }
      )
      .then((response) => {
        if (response.status !== 201) {
          throw new Error({
            message: "Register failed",
            status: response.status,
          });
        }
        setToken(response.data.token);
      })
      .catch((e) => {
        console.log(">> error : ", e.response.data);
      });
  };

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>OKP</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={handleLogin}>Login</button>
        <button onClick={handleLogout}>Logout</button>
        <button onClick={handleRegister}>Register</button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
