import React from "react";
import "../css_styles/TouristCard.css";
import { Link } from "react-router-dom";
const TouristCard = ({ celeb }) => {
  return (
    <div className="tourist">
      <div className="tourist_header">
        <div className="tourist_header1">TOURISMS</div>
        {/* <div className="celeb_header2">DETAIL</div> */}
      </div>
      <div className="tourist_container">
        <Link to="/productivity-detail" state={{ models: 'TOURIST'}}>
          <div className="tourist_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="tourist_text">
              <h2 className="tourist_text1">{celeb.title}</h2>
            </div>
          </div>
        </Link>
        <div className="tourist_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="tourist_text">
            <h2 className="tourist_text1">{celeb.title}</h2>
          </div>
        </div>
        <div className="tourist_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="tourist_text">
            <h2 className="tourist_text1">{celeb.title}</h2>
          </div>
        </div>
        <div className="tourist_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="tourist_text">
            <h2 className="tourist_text1">{celeb.title}</h2>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TouristCard;
