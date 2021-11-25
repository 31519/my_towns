import React from "react";
import "../css_styles/AdminSidebar.css";
import { Link } from "react-router-dom";

const AdminSidebar = ({ tech }) => {
  return (
    <>
      <div className="dashboard">
        <div className="dashboard_header">
          <div className="profile-img">this</div>
          <div className="dashboard_email">
            <h3> cosrumut </h3>
          </div>
          <Link to="/user-profile-edit">
            <div className="dashboard_edit">
              <h3> Edit Profile </h3>
            </div>
          </Link>
        </div>
        <div className="Scroll">
          <div className="dashboard_performance">
            <h3 className="text_header">PERFORMANCE</h3>
            <div className="dashboard_performance_items">
              <div className="dashboard_performance_items1">
                <h3>Charts</h3>
              </div>
              <div className="dashboard_performance_items1">
                <h3>Tables</h3>
              </div>
            </div>
          </div>
          <hr />
          <div className="dashboard_pages">
            <h3>PAGES</h3>
            <hr />
            <div className="dashboard_pages_items">
              <h3 className="text_header">News</h3>
              <Link to="/">
                <div className="dashboard_pages_items1">
                  <h3>Technology</h3>
                </div>
              </Link>

              <Link to="/">
                <div className="dashboard_pages_items1">
                  <h3>Educations</h3>
                </div>
              </Link>

              <Link to="/">
                <div className="dashboard_pages_items1">
                  <h3>Science</h3>
                </div>
              </Link>

              <Link to="/">
                <div className="dashboard_pages_items1">
                  <h3>Business</h3>
                </div>
              </Link>

              <Link to="/">
                <div className="dashboard_pages_items1">
                  <h3>Local News</h3>
                </div>
              </Link>

              <h3 className="text_header">Productivity</h3>

              <Link to="/jobs">
                <div className="dashboard_pages_items1">
                  <h3>Jobs</h3>
                </div>
              </Link>

              <Link to="/reseller">
                <div className="dashboard_pages_items1">
                  <h3>Reseller</h3>
                </div>
              </Link>

              <Link to="/shops">
                <div className="dashboard_pages_items1">
                  <h3>Shops</h3>
                </div>
              </Link>

              <Link to="/advertise">
                <div className="dashboard_pages_items1">
                  <h3>Advertise</h3>
                </div>
              </Link>

              <h3 className="text_header">Luxiery</h3>

              <Link to="/celebrity">
                <div className="dashboard_pages_items1">
                  <h3>Celebrities</h3>
                </div>
              </Link>

              <Link to="/tourist">
                <div className="dashboard_pages_items1">
                  <h3>Tourisms</h3>
                </div>
              </Link>

              <Link to="/hotels">
                <div className="dashboard_pages_items1">
                  <h3>Hotels</h3>
                </div>
              </Link>

              <Link to="/event">
                <div className="dashboard_pages_items1">
                  <h3>Event</h3>
                </div>
              </Link>
            </div>
          </div>
          <div className="dashboard_info">
            <h3>INFO</h3>
          </div>
        </div>
      </div>
    </>
  );
};

export default AdminSidebar;
