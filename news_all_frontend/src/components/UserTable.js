import React from "react";
import "../css_styles/UserTable.css";
const UserTable = () => {
  return (
    <div className="user_table">
        <h2 className="user_table_text">User's List</h2>
        <table className="user_scroll">
            
            <thead>
                <tr className="user_header">
                    <th>user</th>
                    <th>username</th>
                    <th>isApproved</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>cos</td>
                    <td>cosrumut</td>
                    <td>Yes</td>
                </tr>
                <tr>
                    <td>cos</td>
                    <td>cosrumut</td>
                    <td>Yes</td>
                </tr>
                <tr>
                    <td>cos</td>
                    <td>cosrumut</td>
                    <td>Yes</td>
                </tr>
            </tbody>
        </table>
      
    </div>
  );
};

export default UserTable;
