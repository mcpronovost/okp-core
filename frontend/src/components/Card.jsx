import { React } from "react";
import axios from "@/scripts/utils/api.js";

const doCallHandler = () => {
  try {
    axios
      .get(`/api-wagtail/pages/?locale=fr`)
      .then((r) => {
        console.log("r : ", r);
      })
      .catch((e) => {
        console.log("e : ", e);
      });
  } catch (e) {
    console.log("error : ", e);
  }
};

const Card = (props) => {
  return (
    <div>
      <div>
        <div>
          default:{props.children}
        </div>
        <div>
          content:{props.content}
        </div>
        <button onClick={doCallHandler}>Click here</button>
      </div>
    </div>
  );
};

export default Card;
