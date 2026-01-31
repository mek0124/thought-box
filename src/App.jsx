import { Routes, Route } from "react-router-dom";

import Header from './components/header';
import SideNav from './components/sideNav';
import Dashboard from './pages/dashboard';
import Profile from './pages/profile';

export default function App() {
  return (
    <div className="flex flex-col w-full min-h-screen">
      <Header />
      <div className="flex flex-row flex-grow w-full">
        <SideNav />
        <div className="flex flex-col w-full">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </div>
      </div>
    </div>
  );
};