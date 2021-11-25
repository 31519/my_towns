import React from "react";
import "../css_styles/TechList.css";
import Categories from "../components/Categories";
const Footers = () => {
  return (
    <div className="techlist_footer">
      <div className="techlist_footer_items">
        <div className="techlist_footer_items1">
          <div className="techlist_footer_getInTouch">
            <h2>GET IN TOUCH </h2>
          </div>
          <div className="techlist_footer_getInTouch_items">
            <h2>Caroline Colony, Jowai, West Jaintia Hill</h2>
            <h2>@mystardust000</h2>
          </div>
        </div>
        <div className="techlist_footer_items2">
          <Categories/>
          {/* <div className="techlist_footer_category">
            <div className="techlist_footer_category_header">
              <h2>CATEGORIES</h2>
            </div>
            <div className="techlist_footer_category_items">
              <div>
                <h2 className="techlist_footer_category_items1">Science</h2>
              </div>
              <div>
                <h2 className="techlist_footer_category_items1">Health</h2>
              </div>
              <div>
                <h2 className="techlist_footer_category_items1">Technology</h2>
              </div>
              <div>
                <h2 className="techlist_footer_category_items1">Business</h2>
              </div>
            </div>
          </div> */}
        </div>
        <div className="techlist_footer_items3">
          <h2>ASSOCIATES</h2>
        </div>
      </div>
      <div className="techlist_brand">
        <div className="techlist_brand_items">
          <h2 className="techlist_brand1">@mySiteName</h2>
          <h2 className="techlist_brand2">All Right Reserved</h2>
          <h2 className="techlist_brand1">Created by: Stardust</h2>
        </div>
      </div>
    </div>
  );
};

export default Footers;
