import React from "react";
import "../css_styles/Navbars.css";
import { useSelector } from "react-redux";
import PageviewIcon from "@mui/icons-material/Pageview";
import LaptopMacIcon from "@mui/icons-material/LaptopMac";
import AdminSidebar from "../components/AdminSidebar"

const Navbars = () => {

  




  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;
  console.log(userInfo);
  return (
    <div className="header">
      <div className="navbar">
        {/* here */}
        <div className="burger">
          <div className="line1"></div>
          <div className="line2"></div>
          <div className="line3"></div>
        </div>

        {/* <div className="navbar__list">
          <LaptopMacIcon className="navbar__techicon" />
          <h4>Tech</h4>
        </div> */}

        <div className="navbar__input">
          <input className="navbar__search" placeholder="search" />
          <PageviewIcon />
        </div>

        <div className="navbar__logo">
          <div className="navbar__logo__user">
            {userInfo && <h4>{userInfo.username}</h4>}
          </div>
          <div className="navbar__logo__user">
            <h4>My Logo</h4>
          </div>
        </div>

        {/* here */}
        <div class="navbar__link">
          <AdminSidebar/>
      </div>
      </div>
    </div>
  );
};

export default Navbars;
