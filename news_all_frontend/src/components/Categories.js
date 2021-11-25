import React from "react";
import "../css_styles/Categories.css";
import { Link } from "react-router-dom";

const Categories = () => {
  return (
    <div className="techlist_footer_items_component">
      <div className="techlist_footers_category">
        <div className="techlist_footer_category_title">
          <h2>CATEGORIES</h2>
        </div>
        <div className="techlist_footer_category_item">
          <div>
            <Link to="/">
              <h2 className="techlist_footer_category_item1">Science</h2>
            </Link>
          </div>
          <div>
            <Link to="/health-news">
              <h2 className="techlist_footer_category_item1">Health</h2>
            </Link>
          </div>

          <div>
            <Link to="/technology-news">
              <h2 className="techlist_footer_category_item1">Technology</h2>
            </Link>
          </div>

          <div>
            <Link to="/">
              <h2 className="techlist_footer_category_item1">Business</h2>
            </Link>
          </div>

          <div>
            <Link to="/jobs">
              <h2 className="techlist_footer_category_item1">Jobs</h2>
            </Link>
          </div>

          <div>
            <Link to="/tourist">
              <h2 className="techlist_footer_category_item1">Tourisms</h2>
            </Link>
          </div>

          <div>
            <Link to="/celebrity">
              <h2 className="techlist_footer_category_item1">Celebrities</h2>
            </Link>
          </div>

          <div>
            <Link to="/event">
              <h2 className="techlist_footer_category_item1">Event</h2>
            </Link>
          </div>

          <div>
            <Link to="/advertise">
              <h2 className="techlist_footer_category_item1">Advertise</h2>
            </Link>
          </div>

          <div>
            <Link to="/reseller">
              <h2 className="techlist_footer_category_item1">Reseller</h2>
            </Link>
          </div>
          <div>
            <Link to="/hotels">
              <h2 className="techlist_footer_category_item1">Hotels</h2>
            </Link>
          </div>
          <div>
            <Link to="/shops">
              <h2 className="techlist_footer_category_item1">Shops</h2>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Categories;
