import { useState } from "react";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartBar, faChartColumn } from "@fortawesome/free-solid-svg-icons";


export default function SideNav() {
  const [isOpen, setIsOpen] = useState(true);
  const [isActive, setIsActive] = useState(false);

  const handleIsOpen = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="flex flex-col items-start justify-start flex-grow w-1/5">
      <button
        type="button"
        onClick={handleIsOpen}
        className={`${isOpen ? 'text-accent' : 'text-primary'} text-md m-1 py-1 px-2 hover:text-accentHover`}
      >
        {
          isOpen
          ? <FontAwesomeIcon icon={faChartBar} />
          : <FontAwesomeIcon icon={faChartColumn} />
        }
      </button>

      {isOpen && (
        <div className="flex-grow bg-secondary w-full">
          <Link
            to="/"
            className=""
          >
            Dashboard
          </Link>
        </div>
      )}

      {!isOpen && (
        <div className="flex-grow bg-secondary w-16">
          <Link></Link>
        </div>
      )}
    </div>
  );
};
