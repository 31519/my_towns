import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import Cards from "../components/Cards";
import Footers from "../components/Footers";
import Banners from "../components/Banners";

import "../css_styles/TechList.css";
import { listTechs } from "../actions/techActions";

import Categories from "../components/Categories";
import Advertise from "../components/Advertise";
import CelebCarousel from "../components/CelebCarousel";

const techss = {
  title: "title",
  urlToImage:
    "https://staticg.sportskeeda.com/editor/2021/11/caca5-16370851386444-1920.jpg",
  description: "description",
  author: "author",
  content: "content",
};

const TechList = () => {
  const dispatch = useDispatch();
  const techList = useSelector((state) => state.techList);
  const { error, loading, techs } = techList;

  useEffect(() => {
    dispatch(listTechs());
  }, [dispatch]);

  // const [techs, setTechs] = useState([]);
  // useEffect(() => {
  //   async function fetchTech() {
  //     const { data } = await axios.get(
  //       "http://127.0.0.1:8000/api/technology/list/"
  //     );
  //     setTechs(data);
  //   }
  //   fetchTech();
  // }, []);
  // console.log("tech", techs);

  return (
    <>
      <div className="techlist">
        <CelebCarousel celeb={techss}/>
        <Banners />
        <Categories />
        <div className="techlist_headline">
          <div className="techlist_headline1">headline1</div>
          <div className="techlist_headline2">headline2</div>
        </div>

        <div className="techlist_main">
          <div className="techlist_main_inside">
            <div className="techlist_main_text">
              <div className="techlist_main_text1"></div>
              <div className="techlist_main_text2">Latest news</div>
            </div>
            <div className="techlist_main_news">
              <div className="techlist_main_news1">
                {techs.map((tech) => (
                  <Cards key={tech.id} tech={tech} />
                ))}
              </div>

              <div className="techlist_main_news2">
                <div className="techlist_main_ads">
                  {/* <div className="techlist_maid_ads_header">
                    <div className="techlist_maid_ads_header1"></div>
                    <div className="techlist_maid_ads_header2">Advertise</div>
                  </div> */}
                  {/* <div className="techlist_maid_ads_items"></div> */}
                  <Advertise celeb={techss} />
                </div>
              </div>
            </div>
          </div>
        </div>

        <Footers />
      </div>
    </>
  );
};

export default TechList;
