import React from "react";
import "../css_styles/DetailCard.css";
const DetailCard = ({ tech }) => {
  return (
    <div className="detail">
      <div className="detail_container">
        <div className="detail_header">
          <div className="detail_header1"></div>
          <div className="detail_header2">DETAIL</div>
        </div>
        <div className="detail_items">
          <img src={tech.urlToImage} alt="" />
          <div className="detail_text">
            <h2 className="detail_text1">{tech.title}</h2>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DetailCard;
