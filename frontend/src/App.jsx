import { useState } from "react";
import axios from "axios";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/react.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0)

  const handleLogin = () => {
    axios.post("http://localhost:8000/api/v1/auth/login/", {
      username: "mc",
      password: "1"
    }, {
      headers: {
        "Accept-CH": "Sec-CH-UA-Platform"
      }
    })
    .then((response) => {
      console.log(">> response : ", response)
    })
    .catch((error) => {
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
