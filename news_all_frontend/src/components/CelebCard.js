import React from "react";
import "../css_styles/CelebCard.css";
import { Link } from "react-router-dom";
const CelebCard = ({ celeb }) => {
  return (
    <div className="celeb">
      <div className="celeb_header">
        <div className="celeb_header1">LATEST FEATURES</div>
        {/* <div className="celeb_header2">DETAIL</div> */}
      </div>
      <div className="celeb_container">
        <Link to="/productivity-detail" state={{ models: 'CELEB'}}>
          <div className="celeb_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="celeb_text">
              <h2 className="celeb_text1">{celeb.title}</h2>
            </div>
          </div>
        </Link>

        <div className="celeb_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="celeb_text">
            <h2 className="celeb_text1">{celeb.title}</h2>
          </div>
        </div>

        <div className="celeb_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="celeb_text">
            <h2 className="celeb_text1">{celeb.title}</h2>
          </div>
        </div>

        <div className="celeb_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="celeb_text">
            <h2 className="celeb_text1">{celeb.title}</h2>
          </div>
        </div>

        <div className="celeb_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="celeb_text">
            <h2 className="celeb_text1">{celeb.title}</h2>
          </div>
        </div>

        <div className="celeb_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="celeb_text">
            <h2 className="celeb_text1">{celeb.title}</h2>
          </div>
        </div>
        {/* <div className="celeb_items2">
          <img src={celeb.urlToImage} alt="" />
          <div className="celeb_text">
            <h2 className="celeb_text1">{celeb.title}</h2>
            <h2 className="celeb_text1">afjajdflajdfjaldjf</h2>
          </div>
        </div> */}
      </div>
    </div>
  );
};

export default CelebCard;
