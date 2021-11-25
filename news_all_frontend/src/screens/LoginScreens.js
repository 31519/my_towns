import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { userLogin } from "../actions/userActions";

import "../css_styles/LoginScreen.css";

const LoginScreens = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const dispatch = useDispatch();
  // user = user,
  // author = data['author'],
  // title = data['title'],
  // description = data['description'],
  // url= data['url'],
  // urlToImage= data['urlToImage'],
  // publishedAt = data['publishedAt'],
  // content = data['content']

  const submitHandler = (e) => {
    e.preventDefault();
    dispatch(userLogin(username, password));
    console.log("clicked", username);
  };

  return (
    <>
      <div className="login">
        <div className="login_main">
          <div className="login_form">
            <form onSubmit={submitHandler}>
              <div className="login_text">
                <div className="login_text1">LOGIN</div>
              </div>
              <div className="login_container">
                <label>username</label>
                <input
                  id="username"
                  className="input"
                  type="text"
                  placeholder="username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
              </div>
              <div className="login_container">
                <label>password</label>
                <input
                  id="password"
                  className="input"
                  type="password"
                  placeholder="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>

              <div className="login_button">
                <button className="button_input" type="submit">
                  Submit
                </button>
              </div>
            </form>
            <div className="signup_login">
              No Account ? 
              <h2>SignUp</h2>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginScreens;
