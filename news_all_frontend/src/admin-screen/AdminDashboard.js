import React from "react";
import "../css_styles/AdminDashboard.css";
import AdminSidebar from "../components/AdminSidebar";
import PerformanceChart from "../components/PerformanceChart";
import Table from "../components/Table";
import UserTable from "../components/UserTable";

const admin = [
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
const AdminDashboard = ({ tech }) => {
  return (
    <div className="admin">
      <div className="admin_top">Admin Headers</div>

      <div className="admin_main">
        <div className="admin_sidebar">
          <AdminSidebar />
        </div>
        <div className="admin_body">
          <PerformanceChart />
          <div className="admin_status">
            <div className="admin_status1">
              <div className="admin_status1_items">Icon</div>
              <div className="admin_status1_items">
                Visitors
                <br />
                1235
              </div>
            </div>
            <div className="admin_status1">
              <div className="admin_status1_items">Icon</div>
              <div className="admin_status1_items">
                Page Views
                <br />
                1235
              </div>
            </div>
          </div>
          <div className="users_post">
            <h2 className="users_post_text">Local News</h2>
            <Table cat={"Local News"} />

            <h2 className="users_post_text">Jobs</h2>
            <Table cat={"Jobs"}/>
            <h2 className="users_post_text">Advertise</h2>
            <Table cat={"Advertise"}/>
            <h2 className="users_post_text">Shops</h2>
            <Table  cat={"Shops"}/>
            <h2 className="users_post_text">Business</h2>
            <Table  cat={"Business"}/>
            <h2 className="users_post_text">Celebrities</h2>
            <Table  cat={"Celebrities"}/>
            <h2 className="users_post_text">Hotels</h2>
            <Table  cat={"Hotels"}/>
            <h2 className="users_post_text">Tourisms</h2>
            <Table  cat={"Tourisms"}/>
            
          </div>
        </div>

        <div className="users">
          
          <UserTable/>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
