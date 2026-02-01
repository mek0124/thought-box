import { Routes, Route } from "react-router-dom";

import Header from './components/header';
import SideNav from './components/sideNav';
import Dashboard from './pages/dashboard';
import Profile from './pages/profile';
import { useEffect, useState } from "react";

export default function App() {
  const [foundUser, setFoundUser] = useState(null);

  useEffect(() => {
    async function fetchUser() {
      try {
        const response = window.localStorage.getItem("user");
        const parsedResponse = response ? JSON.parse(response) : null;

        if (parsedResponse) {
          setFoundUser(parsedResponse);
        }
      } catch (err) {
        console.error(err);
        setFoundUser(null);
      }
    };

    fetchUser();
  }, []);

  return (
    <div className="flex flex-col w-full min-h-screen">
      <Header />
      <div className="flex flex-row flex-grow w-full">
        <SideNav />
        <div className="flex flex-col w-full">
          <Routes>
            <Route path="/" element={<Dashboard user={foundUser} />} />
            <Route path="/profile" element={<Profile user={foundUser} />} />
          </Routes>
        </div>
      </div>
    </div>
  );
};