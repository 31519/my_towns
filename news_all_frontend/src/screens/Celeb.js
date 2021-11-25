import React from "react";
import "../css_styles/Celeb.css";
import CelebCard from "../components/CelebCard";
import Event from "../components/Event";
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
const Celeb = () => {
  return (
    <div>
      <CelebCarousel celeb={celeb}/>
      <Banners/>
      <Categories/>
      <div className="celeb_screen">
        <div className="celeb_song">
          <CelebCard celeb={celeb} />
        </div>
        <div className="celeb_event">
          <Event celeb={celeb} />
        </div>
      </div>
      <Footers/>
    </div>
  );
};

export default Celeb;
