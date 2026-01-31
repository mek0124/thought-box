import { useState, useEffect } from "react";

import AppIcon from '../assets/original.png';

export default function Header() {
  const [cTime, setCTime] = useState('');
  const [cDate, setCDate] = useState('');
  const [isHour12, setIsHour12] = useState(false);

  useEffect(() => {
    function updateClock() {
      const now = new Date();
      const timeOptions = { hour12: isHour12, hour: '2-digit', minute: '2-digit', second: '2-digit' };
      const dateOptions = { year: 'numeric', month: 'short', day: 'numeric' };
      
      setCTime(now.toLocaleTimeString([], timeOptions));
      setCDate(now.toLocaleDateString([], dateOptions));
    }

    updateClock();
    const intervalId = setInterval(updateClock, 1000);
    return () => clearInterval(intervalId);
  }, [isHour12]);

  const handleHour12Switch = (format12) => {
    setIsHour12(format12);
  };

  return (
    <div className="flex flex-row items-center justify-between w-full border-b-2 border-b-primary px-2 py-1">
      <div className="flex flex-row items-center">
        <img
          src={AppIcon}
          alt="Thought Box App Icon"
          width="60"
          height="60"
          className="rounded-full mr-2"
        />
        <h1 className="font-bold italic text-lg text-primary">
          Thought Box
        </h1>
      </div>

      <div className="flex flex-row items-center gap-2">
        <div className="flex flex-col items-center border border-primary rounded-md overflow-hidden">
          <button
            type="button"
            onClick={() => handleHour12Switch(true)}
            className={`text-xs px-1 py-1 ${isHour12 ? 'bg-primary text-text_on_accent' : 'bg-transparent text-text_primary'}`}
          >
            12H
          </button>
          <button
            type="button"
            onClick={() => handleHour12Switch(false)}
            className={`text-xs px-1 py-1 ${!isHour12 ? 'bg-primary text-text_on_accent' : 'bg-transparent text-text_primary'}`}
          >
            24H
          </button>
        </div>

        <div className="flex flex-col items-end w-32">
          <span className="italic text-sm text-text_primary">
            {cTime}
          </span>
          <span className="italic text-sm text-text_primary">
            {cDate}
          </span>
        </div>
      </div>
    </div>
  );
};