import React from "react";
import "../css_styles/Tourisms.css";
import ShopCard from "../components/ShopCard";
import Jobs from "../components/Jobs";
import Footers from "../components/Footers";
import Banners from "../components/Banners";
import Categories from "../components/Categories";
import CelebCarousel from "../components/CelebCarousel";

const celeb = {
  title: "title",
  urlToImage:
    "https://staticg.sportskeeda.com/editor/2021/11/caca5-16370851386444-1920.jpg",
  description: "description",
  author: "author",
  content: "content",
};
const Shops = () => {
  return (
    <div>
      <CelebCarousel celeb={celeb}/>
      <Banners/>
      <Categories/>
      <div className="tourist_screen">
        <div className="tourist_main">
          <ShopCard celeb={celeb} />
        </div>
        <div className="tourist_event">
          <Jobs celeb={celeb} />
        </div>
      </div>
      <Footers/>
    </div>
  );
};

export default Shops;
