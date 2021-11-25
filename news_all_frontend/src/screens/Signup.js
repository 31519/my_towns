import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { userLogin } from "../actions/userActions";

import "../css_styles/Signup.css";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

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
      <div className="signup">
        <div className="signup_main">
          <div className="signup_form">
            <form onSubmit={submitHandler}>
              <div className="signup_text">
                <div className="signup_text1">LOGIN</div>
              </div>
              <div className="signup_container">
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
              <div className="signup_container">
                <label>email</label>
                <input
                  id="email"
                  className="input"
                  type="email"
                  placeholder="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>

              <div className="signup_container">
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

              <div className="signup_container">
                <label>confirm password</label>
                <input
                  id="password"
                  className="input"
                  type="password"
                  placeholder="confirm password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                />
              </div>

              <div className="signup_button">
                <button className="button_input" type="submit">
                  Submit
                </button>
              </div>
            </form>
            <div className="signup_login">
              Allready have an account ?
              <h2>Sign In</h2>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Signup;
