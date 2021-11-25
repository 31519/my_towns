import React from "react";
import "../css_styles/UserDashboard.css";
import AdminSidebar from "../components/AdminSidebar";
import PerformanceChart from "../components/PerformanceChart";
import Table from "../components/Table";
import PostTable from "../components/PostTable";

const tech = [
  {
    title: "title",
    urlToImage:
      "https://staticg.sportskeeda.com/editor/2021/11/caca5-16370851386444-1920.jpg",
    description: "description",
    author: "author",
    content: "content",
  },
  {
    title: "title",
    urlToImage:
      "https://staticg.sportskeeda.com/editor/2021/11/caca5-16370851386444-1920.jpg",
    description: "description",
    author: "author",
    content: "content",
  },
];
const UserDashboard= ({ tech }) => {
  return (
    <div className="user_dashboard">
      <div className="user_dashboard_top">User Dashboard</div>

      <div className="user_dashboard_main">
        <div className="user_dashboard_sidebar">
          <AdminSidebar />
        </div>
        <div className="user_dashboard_body">
          <PerformanceChart />
          <div className="user_dashboard_status">
            <div className="user_dashboard_status1">
              <div className="user_dashboard_status1_items">Icon</div>
              <div className="user_dashboard_status1_items">
                Visitors
                <br />
                1235
              </div>
            </div>
            <div className="user_dashboard_status1">
              <div className="user_dashboard_status1_items">Icon</div>
              <div className="user_dashboard_status1_items">
                Page Views
                <br />
                1235
              </div>
            </div>
          </div>
          <div className="user_dashboard_post">

            <h2 className="user_dashboard_post_text">Jobs</h2>
            <PostTable cat={"Jobs"}/>
            <h2 className="user_dashboard_post_text">Advertise</h2>
            <PostTable cat={"Advertise"} />
            <h2 className="user_dashboard_post_text">Shops</h2>
            <PostTable cat={"Shops"} />
            <h2 className="user_dashboard_post_text">Business</h2>
            <PostTable cat={"Business"} />
            <h2 className="user_dashboard_post_text">Celebrities</h2>
            <PostTable  cat={"Celebrities"}/>
            <h2 className="user_dashboard_post_text">Hotels</h2>
            <PostTable cat={"Hotels"} />
            <h2 className="user_dashboard_post_text">Tourisms</h2>
            <PostTable  cat={"Tourisms"}/>
            
          </div>
        </div>
        <div className="users">
            Hi
        </div>
      </div>
    </div>
  );
};

export default UserDashboard;
