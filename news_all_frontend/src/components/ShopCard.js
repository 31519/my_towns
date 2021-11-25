import React from "react";
import "../css_styles/ShopCard.css";
import { Link } from "react-router-dom";

const ShopCard = ({ celeb }) => {
  return (
    <div className="shop">
      <div className="shop_header">
        <div className="tourist_header1">SHOPS</div>
        {/* <div className="celeb_header2">DETAIL</div> */}
      </div>
      <div className="shop_container">
        <Link to="/productivity-detail" state={{ models: 'SHOP'}}>
          <div className="shop_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="shop_text">
              <h2 className="shop_text1">{celeb.title}</h2>
            </div>
          </div>
        </Link>
        <div className="shop_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="shop_text">
            <h2 className="shop_text1">{celeb.title}</h2>
          </div>
        </div>

        <div className="shop_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="shop_text">
            <h2 className="shop_text1">{celeb.title}</h2>
          </div>
        </div>

        <div className="shop_items1">
          <img src={celeb.urlToImage} alt="" />
          <div className="shop_text">
            <h2 className="shop_text1">{celeb.title}</h2>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ShopCard;
