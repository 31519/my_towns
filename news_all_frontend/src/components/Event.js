import React from "react";
import "../css_styles/Event.css";
import { Link } from "react-router-dom";
const Event = ({ celeb }) => {
  return (
    <div className="event_boss">
      <div className="event">
        <div className="event_header">
          <div className="event_header1">Event</div>
          {/* <div className="celeb_header2">DETAIL</div> */}
        </div>
        <div className="event_container">
          <Link to="/productivity-detail" state={{ models: 'EVENT'}}>
            <div className="event_items1">
              <img src={celeb.urlToImage} alt="" />
              <div className="event_text">
                <h2 className="event_text1">{celeb.title}</h2>
              </div>
            </div>
          </Link>
          <div className="event_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="event_text">
              <h2 className="event_text1">{celeb.title}</h2>
            </div>
          </div>
          <div className="event_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="event_text">
              <h2 className="event_text1">{celeb.title}</h2>
            </div>
          </div>
          <div className="event_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="event_text">
              <h2 className="event_text1">{celeb.title}</h2>
            </div>
          </div>
          <div className="event_items1">
            <img src={celeb.urlToImage} alt="" />
            <div className="event_text">
              <h2 className="event_text1">{celeb.title}</h2>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Event;
