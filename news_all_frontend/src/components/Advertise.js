import React from "react";
import "../css_styles/Advertise.css";
import {Link} from 'react-router-dom'
const Advertise = ({ celeb }) => {
  return (
    <div className="advertise">
      <Link to='/productivity-detail'  state={{ models: 'ADVERTISE'}}>
      <div className="advertise_container">
        <div className="advertise_header">
          <div className="advertise_header1"></div>
          <div className="advertise_header2">Advertise</div>
        </div>
        <div className="advertise_items">
          <img src={celeb.urlToImage} alt="" />
          <div className="advertise_text">
            <h2 className="advertise_text1">{celeb.title}</h2>
          </div>
        </div>
      </div>
      </Link>
    </div>
  );
};

export default Advertise;
