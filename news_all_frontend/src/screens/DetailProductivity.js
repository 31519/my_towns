import React from "react";
import Footers from "../components/Footers";
import Advertise from "../components/Advertise";
import "../css_styles/DetailProductivity.css";
import ProductivityDetail from "../components/ProductivityDetail";
import {useLocation} from  'react-router-dom'


const techs = {
  title: "title",
  urlToImage:
    "https://staticg.sportskeeda.com/editor/2021/11/caca5-16370851386444-1920.jpg",
  description: "description",
  author: "author",
  content: "content",
};
const DetailProductiivity = () => {
  const location = useLocation()
  const {models} = location.state

  return (
    <div>
      <div className="productivity_main">
        <div className="productivity_cards">
          <ProductivityDetail tech="{techs}" models={models}/>
        </div>
        <div className="productivity_advertise">
          <Advertise tech={techs} />
        </div>
      </div>

      <Footers />
    </div>
  );
};

export default DetailProductiivity;
