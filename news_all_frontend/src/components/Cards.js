import React from "react";
import "../css_styles/cards.css";
import { Link } from "react-router-dom";

const Cards = ({ tech }) => {
  return (
    <Link to="/news-detail">
      <div className="cards">
        <img src={tech.urlToImage} alt="" />

        <div className="cards_text">
          <h2 className="cards__title">{tech.title}</h2>
        </div>
      </div>
    </Link>
  );
};

export default Cards;
