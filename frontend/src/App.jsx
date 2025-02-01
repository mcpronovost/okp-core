import { useState } from "react";
import axios from "axios";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/react.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0)
  const [token, setToken] = useState(null)

  const handleLogin = () => {
    axios.post("http://localhost:8000/api/v1/auth/login/", {
      username: "mc",
      password: "1"
    }, {
      headers: {
        "Accept-CH": "Sec-CH-UA-Platform"
      }
    }).then((response) => {
      if (response.status !== 200) {
        throw new Error("Login failed")
      }
      setToken(response.data.token)
    }).catch((error) => {
      console.log(">> error : ", error)
    })
  }

  const handleLogout = () => {
    axios.post("http://localhost:8000/api/v1/auth/logout/", null, {
      headers: {
        "Authorization": `okp ${token}`
      }
    }).then((response) => {
      if (response.status !== 204) {
        throw new Error("Logout failed")
      }
      setToken(null)
    }).catch((error) => {
      console.log(">> error : ", error)
    })
  }

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
        <button onClick={handleLogin}>
          Login
        </button>
        <button onClick={handleLogout}>
          Logout
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
