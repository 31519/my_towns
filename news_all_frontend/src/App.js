import "./App.css";
import { HashRouter as Router, Routes, Route } from "react-router-dom";
import Navbars from "./navbars/Navbars";
import TechList from "./screens/TechLIst";
import TechCreate from "./admin-screen/TechCreate";
import LoginScreens from "./screens/LoginScreens"
import DetailTechList from "./screens/DetailTechList";
import Celeb from "./screens/Celeb";
import Tourisms from "./screens/Tourisms";
import DetailEntertainment from "./screens/DetailEntertainment";
import Shops from "./screens/Shops";
import DetailProductiivity from "./screens/DetailProductivity";
import AdminDashboard from "./admin-screen/AdminDashboard";
import Signup  from "./screens/Signup"
import UserDashboard from "./screens/UserDashboard";
import Hotels from "./screens/Hotels"
import JobsScreen from "./screens/JobsScreen";
import AdvertiseScreen from "./screens/AdvertiseScreen";
import ResellerScreen from "./screens/ResellerScreen";
import EventScreen from "./screens/EventScreen";
import ProductivityCreate from "./admin-screen/ProductivityCreate";
import UserPostUpdate  from "./screens/UserPostUpdate"
import UserProfileEdit from "./screens/UserProfileEdit";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbars />
        <Routes>


          <Route path="login" element={<LoginScreens/>} />
          <Route path="signup" element={<Signup/>} />
          <Route path="my-dashboard" element={<UserDashboard/>} />

          <Route path="/" element={<TechList />} exact />

          <Route path="celebrity" element={<Celeb/>} />
          <Route path="tourist" element={<Tourisms/>} />
          <Route path="shops" element={<Shops/>} />
          <Route path="hotels" element={<Hotels/>} />
          <Route path="jobs" element={<JobsScreen/>} />
          <Route path="advertise" element={<AdvertiseScreen/>} />
          <Route path="reseller" element={<ResellerScreen/>} />
          <Route path="event" element={<EventScreen/>} />
          
          <Route path="news-detail" element={<DetailTechList/>} />
          <Route path="productivity-detail" element={<DetailProductiivity/>} />
          <Route path="celebrity-detail" element={<DetailEntertainment/>} />

          <Route path="admin-dashboard" element={<AdminDashboard/>} />
          <Route path="tech-create" element={<TechCreate/>} />
          <Route path="productivity-create" element={<ProductivityCreate/>} />
          <Route path="user-post-create" element={<UserPostUpdate/>} />
          <Route path="user-profile-edit" element={<UserProfileEdit/>} />

        </Routes>
      </Router>
    </div>
  );
}

export default App;
