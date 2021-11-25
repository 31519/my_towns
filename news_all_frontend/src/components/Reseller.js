import React from "react";
import "../css_styles/Reseller.css";
import { Link } from "react-router-dom";

const Reseller = ({ celeb }) => {
  return (
    <div className="reseller_boss">
      <div className="reseller">
        <div className="reseller_header">
          <div className="reseller_header1">RESELLER</div>
          {/* <div className="celeb_header2">DETAIL</div> */}
        </div>

        <div className="reseller_container">
          <Link to="/productivity-detail" state={{ models: 'RESELLER'}}>
            <div className="reseller_items1">
              <img src={celeb.urlToImage} alt="" />
              <div className="reseller_text">
                <h2 className="reseller_text1">{celeb.title}</h2>
              </div>
            </div>
          </Link>
          <div className="reseller_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="reseller_text">
              <h2 className="reseller_text1">{celeb.title}</h2>
            </div>
          </div>
          <div className="reseller_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="reseller_text">
              <h2 className="reseller_text1">{celeb.title}</h2>
            </div>
          </div>
          <div className="reseller_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="reseller_text">
              <h2 className="reseller_text1">{celeb.title}</h2>
            </div>
          </div>
          <div className="reseller_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="reseller_text">
              <h2 className="reseller_text1">{celeb.title}</h2>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Reseller;
