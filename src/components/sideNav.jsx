import { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartBar, faChartColumn, faCubes, faUser, faGear } from "@fortawesome/free-solid-svg-icons";


export default function SideNav() {
  const [isOpen, setIsOpen] = useState(true);
  const [isActive, setIsActive] = useState(false);
  const location = useLocation();

  const handleIsOpen = () => {
    setIsOpen(!isOpen);
  };

  const isLinkActive = (path) => {
    return location.pathname === path;
  };

  return (
    <div className="flex flex-col items-start justify-start flex-grow pt-1">
      <div className="flex flex-col w-6 justify-center items-center">
        <button
          type="button"
          onClick={handleIsOpen}
          className={`${isOpen ? 'text-accent' : 'text-primary'} text-md hover:text-accentHover`}
        >
          {
            isOpen
            ? <FontAwesomeIcon icon={faChartBar} />
            : <FontAwesomeIcon icon={faChartColumn} />
          }
        </button>
      </div>

      {isOpen && (
        <div className="flex flex-col h-full justify-center items-center w-[10em]">
          <div className="flex-grow flex-cl w-full justify-center items-center">
            <Link
              to="/"
              className={`${isLinkActive('/') ? 'text-accent' : 'text-accent_hover'}`}
            >
              <FontAwesomeIcon icon={faCubes} className="mr-1" />

              Dashboard
            </Link>
          </div>

          <div className="flex-col w-full h-16 border-t-2 border-t-border flex items-start justify-evenly">
            <Link
              to="/profile"
              className={`${isLinkActive('/profile') ? 'text-accent' : 'text-accent_hover'}`}
            >
              <FontAwesomeIcon icon={faUser} />

              Profile
            </Link>

            <Link
              to="/settings"
              className={`${isLinkActive('/settings') ? 'text-accent' : 'text-accent_hover'}`}
            >
              <FontAwesomeIcon icon={faGear} />

              Settings
            </Link>
          </div>
        </div>
      )}

      {!isOpen && (
        <div className="flex flex-col h-full w-full justify-center items-center">
          <div className="flex-grow">
            <Link
              to="/"
              className={`${isLinkActive('/') ? 'text-accent' : 'text-accent_hover'}`}
            >
              <FontAwesomeIcon icon={faCubes} />
            </Link>
          </div>

          <div className="flex-col h-16 justify-start border-t-2 border-t-border flex items-start">
            <Link
              to="/profile"
              className={`${isLinkActive('/profile') ? 'text-accent' : 'text-accent_hover'}`}
            >
              <FontAwesomeIcon icon={faUser} />
            </Link>

            <Link
              to="/settings"
              className={`${isLinkActive('/settings') ? 'text-accent' : 'text-accent_hover'}`}
            >
              <FontAwesomeIcon icon={faGear} />
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};