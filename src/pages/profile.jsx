


export default function Profile({ user }) {
  return (
    <div className="flex flex-col items-center justify-evenly w-full flex-grow border-l-2 border-l-primary">
      <div className="flex flex-row items-center justify-evenly w-[80%] h-[40em] bg-surface_glass rounded-xl shadow-glow shadow-xl">
        <div className="flex flex-col items-start justify-start w-[45%] h-[35em] border-2 border-accent rounded-xl">
          <h3 className="text-text_primary text-lg text-start w-full ml-2">
            Profile Details
          </h3>

          <div className="flex flex-col items-center justify-evenly w-full flex-grow border-t-2 border-t-border rounded-xl">
            <div className="flex flex-row items-center justify-center w-[90%]">
              <label
                htmlFor="username"
                className="text-sm text-text_secondary w-1/5 pt-1"
              >
                Username
              </label>

              <input
                type="text"
                name="username"
                value={user ? user.username : "john_or_jane_doe123" }
                onChange=""
                className="border-b-2 border-b-accent rounded-sm bg-transparent text-md text-end w-[60%] text-text_muted text-sm pr-1"
              />
            </div>
          </div>
        </div>

        <div className="flex flex-col items-center justify-center w-[45%] h-[35em] border-2 border-accent rounded-xl">
          <h3 className="text-text_primary text-lg text-start w-full ml-2">
            Profile Settings
          </h3>

          <div className="flex flex-col items-center justify-center gap-5 w-full flex-grow border-t-2 border-t-border rounded-xl">
            <div className="flex flex-row items-center justify-center w-[90%]">
              <label
                htmlFor="fontFamily"
                className="text-sm text-text_secondary w-1/5 pt-1"
              >
                Font Family
              </label>

              <input
                type="text"
                name="fontFamily"
                value={user ? user.settings.fontFamily : "Times New Roman" }
                onChange=""
                className="border-b-2 border-b-accent rounded-sm bg-transparent text-md text-end w-[60%] text-text_muted text-sm pr-1"
              />
            </div>

            <div className="flex flex-row items-center justify-center w-[90%]">
              <label
                htmlFor="fontSize"
                className="text-sm text-text_secondary w-1/5 pt-1"
              >
                Font Size
              </label>

              <input
                type="text"
                name="fontSize"
                value={user ? user.settings.fontSize : "12" }
                onChange=""
                className="border-b-2 border-b-accent rounded-sm bg-transparent text-md text-end w-[60%] text-text_muted text-sm pr-1"
              />
            </div>

            <div className="flex flex-row items-center justify-center w-[90%]">
              <label
                htmlFor="fontStyle"
                className="text-sm text-text_secondary w-1/5 pt-1"
              >
                Font Style
              </label>

              <input
                type="text"
                name="fontStyle"
                value={user ? user.settings.fontStyle : "normal" }
                onChange=""
                className="border-b-2 border-b-accent rounded-sm bg-transparent text-md text-end w-[60%] text-text_muted text-sm pr-1"
              />
            </div>

            <div className="flex flex-row items-center justify-center w-[90%]">
              <label
                htmlFor="fontColor"
                className="text-sm text-text_secondary w-1/5 pt-1"
              >
                Font Color
              </label>

              <input
                type="text"
                name="fontColor"
                value={user ? user.settings.fontColor : "Purple" }
                onChange=""
                className="border-b-2 border-b-accent rounded-sm bg-transparent text-md text-end w-[60%] text-text_muted text-sm pr-1"
              />
            </div>
          </div>
        </div>
      </div>

      <div className="flex flex-row items-center justify-evenly w-[50%]">
        <button
          type="button"
          className="border-2 border-primary rounded-md px-8 py-2 text-error hover:bg-red-900"
        >
          Reset Profile
        </button>

        <button
          type="button"
          className="border-2 border-primary rounded-md px-8 py-2 text-success hover:bg-green-900"
        >
          Update Profile
        </button>
      </div>
    </div>
  );
};
