import React from "react";
import "../css_styles/Table.css";
import { Link } from "react-router-dom";
const Table = ({ cat }) => {

    const cats = cat
    
  return (
      
    <div className="table">
      <table className="table_scroll">
        <thead>
          <tr id="header">
            <th className="profile">profile</th>
            <th className="user">username</th>
            <th className="titles">title</th>
            <th className="isApproved">approve</th>
            <th className="edit">edit</th>
            <th className="delete">delete</th>
          </tr>
        </thead>
        <tbody>
          {/* <tr>
                    <td><div className="text_wrap1">asdsfdfsdjs</div></td>
                    <td><div className="text_wrap2">tilasjfldjs</div></td>
                    <td><div className="text_wrap3">titdsfljfaksjflgghfhgfghfghfhgfhfhfhgfhajsfklajsfljalsjflasjflasjflkajsfjlasdjs</div></td>
                    <td><div className="text_wrap4">titlldjs</div></td>
                    <td><div className="text_wrap5">titlfajfldjs</div></td>
                    <td><div className="text_wrap6">tfl;asjfldjs</div></td>
                </tr> */}
          <tr>
            <td>hi</td>
            <td>hi</td>
            <td>title</td>
            <td>hi</td>
            <Link to="/productivity-create" state={{ models:`${cats}`, }}>
              <td>hi</td>
            </Link>
            <td>hi</td>
          </tr>
          <tr>
            <td>hi</td>
            <td>hi</td>
            <td>title</td>
            <td>hi</td>
            <td>hi</td>
            <td>hi</td>
          </tr>
          <tr>
            <td>hi</td>
            <td>hi</td>
            <td>title</td>
            <td>hi</td>
            <td>hi</td>
            <td>hi</td>
          </tr>
          <tr>
            <td>hi</td>
            <td>hi</td>
            <td>title</td>
            <td>hi</td>
            <td>hi</td>
            <td>hi</td>
          </tr>
          <tr>
            <td>hi</td>
            <td>hi</td>
            <td>title</td>
            <td>hi</td>
            <td>hi</td>
            <td>hi</td>
          </tr>
          <tr>
            <td>hi</td>
            <td>hi</td>
            <td>title</td>
            <td>hi</td>
            <td>hi</td>
            <td>hi</td>
          </tr>
          <tr>
            <td>hi</td>
            <td>hi</td>
            <td>title</td>
            <td>hi</td>
            <td>hi</td>
            <td>hi</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default Table;
