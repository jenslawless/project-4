import React from "react";

function NavBar() {
  return (
    <div class="flex flex-col fixed left-0 items-center w-20 pt-8 h-screen  text-gray-700 bg-zinc-600 m-0">
      <a
        class="flex items-center justify-center w-12 h-12 m-2 bg-neutral-300 hover:bg-white"
        href=""
      >
        <svg
          class="w-10 h-10 stroke-current"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
      </a>
      <p class="  items-center text-s text-gray-300  ">Account</p>
      <div class="flex flex-col items-center border-t border-gray-300">
        <a
          class="flex items-center justify-center w-12 h-12 m-2 bg-neutral-300 hover:bg-white"
          href="/"
        >
          <svg
            class="w-10 h-10 stroke-current"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke="#CCCCCC"
              stroke-width="0.048"
            ></g>
            <g id="SVGRepo_iconCarrier">
              {" "}
              <path
                d="M19.8978 16H7.89778C6.96781 16 6.50282 16 6.12132 16.1022C5.08604 16.3796 4.2774 17.1883 4 18.2235"
                stroke="#1C274D"
                stroke-width="1.5"
              ></path>{" "}
              <path
                d="M8 7H16"
                stroke="#1C274D"
                stroke-width="1.5"
                stroke-linecap="round"
              ></path>{" "}
              <path
                d="M8 10.5H13"
                stroke="#1C274D"
                stroke-width="1.5"
                stroke-linecap="round"
              ></path>{" "}
              <path
                d="M19.5 19H8"
                stroke="#1C274D"
                stroke-width="1.5"
                stroke-linecap="round"
              ></path>{" "}
              <path
                d="M10 22C7.17157 22 5.75736 22 4.87868 21.1213C4 20.2426 4 18.8284 4 16V8C4 5.17157 4 3.75736 4.87868 2.87868C5.75736 2 7.17157 2 10 2H14C16.8284 2 18.2426 2 19.1213 2.87868C20 3.75736 20 5.17157 20 8M14 22C16.8284 22 18.2426 22 19.1213 21.1213C20 20.2426 20 18.8284 20 16V12"
                stroke="#1C274D"
                stroke-width="1.5"
                stroke-linecap="round"
              ></path>{" "}
            </g>
          </svg>
        </a>
      </div>
      <p class="  items-center text-s text-gray-300  ">Courses</p>
      {/* 3 - Tasks */}
      <div class="flex flex-col items-center border-t border-gray-300">
        <a
          class="flex items-center justify-center w-12 h-12 m-2 bg-neutral-300 hover:bg-white"
          href="/tasks"
        >
          <svg
            class="h-10 w-10 stroke-current"
            viewBox="0 0 512 512"
            version="1.1"
            fill="#000000"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></g>
            <g id="SVGRepo_iconCarrier">
              {" "}
              <title>tasks-all</title>{" "}
              <g
                id="Page-1"
                stroke="none"
                stroke-width="1"
                fill="none"
                fill-rule="evenodd"
              >
                {" "}
                <g
                  id="Combined-Shape"
                  fill="#000000"
                  transform="translate(70.530593, 46.125620)"
                >
                  {" "}
                  <path d="M185.469407,39.207713 L356.136074,39.207713 L356.136074,81.8743797 L185.469407,81.8743797 L185.469407,39.207713 Z M185.469407,188.541046 L356.136074,188.541046 L356.136074,231.207713 L185.469407,231.207713 L185.469407,188.541046 Z M185.469407,337.87438 L356.136074,337.87438 L356.136074,380.541046 L185.469407,380.541046 L185.469407,337.87438 Z M119.285384,-7.10542736e-15 L144.649352,19.5107443 L68.6167605,118.353113 L2.84217094e-14,58.3134476 L21.0721475,34.2309934 L64.0400737,71.8050464 L119.285384,-7.10542736e-15 Z M119.285384,149.333333 L144.649352,168.844078 L68.6167605,267.686446 L2.84217094e-14,207.646781 L21.0721475,183.564327 L64.0400737,221.13838 L119.285384,149.333333 Z M119.285384,298.666667 L144.649352,318.177411 L68.6167605,417.01978 L2.84217094e-14,356.980114 L21.0721475,332.89766 L64.0400737,370.471713 L119.285384,298.666667 Z">
                    {" "}
                  </path>{" "}
                </g>{" "}
              </g>{" "}
            </g>
          </svg>
        </a>
      </div>
      <p class="  items-center text-s text-gray-300  ">Tasks</p>
      <div class="flex flex-col items-center border-t border-gray-300">
        <a
          class="flex items-center justify-center w-12 h-12 m-2 bg-neutral-300 hover:bg-white"
          href="/calendar"
        >
          <svg
            class="w-10 h-10 stroke-current"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></g>
            <g id="SVGRepo_iconCarrier">
              {" "}
              <path
                d="M2 12C2 8.22876 2 6.34315 3.17157 5.17157C4.34315 4 6.22876 4 10 4H14C17.7712 4 19.6569 4 20.8284 5.17157C22 6.34315 22 8.22876 22 12V14C22 17.7712 22 19.6569 20.8284 20.8284C19.6569 22 17.7712 22 14 22H10C6.22876 22 4.34315 22 3.17157 20.8284C2 19.6569 2 17.7712 2 14V12Z"
                stroke="#1C274C"
                stroke-width="1.5"
              ></path>{" "}
              <path
                d="M7 4V2.5"
                stroke="#1C274C"
                stroke-width="1.5"
                stroke-linecap="round"
              ></path>{" "}
              <path
                d="M17 4V2.5"
                stroke="#1C274C"
                stroke-width="1.5"
                stroke-linecap="round"
              ></path>{" "}
              <path
                d="M2.5 9H21.5"
                stroke="#1C274C"
                stroke-width="1.5"
                stroke-linecap="round"
              ></path>{" "}
              <path
                d="M18 17C18 17.5523 17.5523 18 17 18C16.4477 18 16 17.5523 16 17C16 16.4477 16.4477 16 17 16C17.5523 16 18 16.4477 18 17Z"
                fill="#1C274C"
              ></path>{" "}
              <path
                d="M18 13C18 13.5523 17.5523 14 17 14C16.4477 14 16 13.5523 16 13C16 12.4477 16.4477 12 17 12C17.5523 12 18 12.4477 18 13Z"
                fill="#1C274C"
              ></path>{" "}
              <path
                d="M13 17C13 17.5523 12.5523 18 12 18C11.4477 18 11 17.5523 11 17C11 16.4477 11.4477 16 12 16C12.5523 16 13 16.4477 13 17Z"
                fill="#1C274C"
              ></path>{" "}
              <path
                d="M13 13C13 13.5523 12.5523 14 12 14C11.4477 14 11 13.5523 11 13C11 12.4477 11.4477 12 12 12C12.5523 12 13 12.4477 13 13Z"
                fill="#1C274C"
              ></path>{" "}
              <path
                d="M8 17C8 17.5523 7.55228 18 7 18C6.44772 18 6 17.5523 6 17C6 16.4477 6.44772 16 7 16C7.55228 16 8 16.4477 8 17Z"
                fill="#1C274C"
              ></path>{" "}
              <path
                d="M8 13C8 13.5523 7.55228 14 7 14C6.44772 14 6 13.5523 6 13C6 12.4477 6.44772 12 7 12C7.55228 12 8 12.4477 8 13Z"
                fill="#1C274C"
              ></path>{" "}
            </g>
          </svg>
        </a>
      </div>
      <p class="  items-center text-s text-gray-300  ">Calendar</p>
      <div class="flex flex-col items-center border-t border-gray-300">
        <a
          class="flex items-center justify-center w-12 h-12 m-2 bg-neutral-300 hover:bg-white"
          href="/messages"
        >
          <svg
            class="h-10 w-10 stroke-current"
            viewBox="0 0 192 192"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></g>
            <g id="SVGRepo_iconCarrier">
              <path
                fill="#000000"
                d="M18.5 46v-6a6 6 0 0 0-4.243 10.243L18.5 46ZM42 52h104V40H42v12Zm118 14v60h12V66h-12Zm-14 74H62v12h84v-12ZM42 40H18.5v12H42V40Zm6 86V76.127H36V126h12ZM14.257 50.243l18.814 18.813 8.485-8.485-18.813-18.814-8.486 8.486ZM48 76.127a22 22 0 0 0-6.444-15.556l-8.485 8.485A10 10 0 0 1 36 76.127h12ZM62 140c-7.732 0-14-6.268-14-14H36c0 14.359 11.64 26 26 26v-12Zm98-14c0 7.732-6.268 14-14 14v12c14.359 0 26-11.641 26-26h-12Zm-14-74c7.732 0 14 6.268 14 14h12c0-14.36-11.641-26-26-26v12Z"
              ></path>
              <path
                stroke="#000000"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="12"
                d="M66 84h76m-76 24h44"
              ></path>
            </g>
          </svg>
        </a>
      </div>
      <p class=" items-center text-s text-gray-300 ">Messages</p>
      <div class="flex flex-col items-center border-t border-gray-300">
        <a
          class="flex items-center justify-center w-12 h-12 m-2 bg-neutral-300 hover:bg-white"
          href="/help"
        >
          <svg
            class="w-10 h-10"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></g>
            <g id="SVGRepo_iconCarrier">
              <path d="M12 4C9.243 4 7 6.243 7 9h2c0-1.654 1.346-3 3-3s3 1.346 3 3c0 1.069-.454 1.465-1.481 2.255-.382.294-.813.626-1.226 1.038C10.981 13.604 10.995 14.897 11 15v2h2v-2.009c0-.024.023-.601.707-1.284.32-.32.682-.598 1.031-.867C15.798 12.024 17 11.1 17 9c0-2.757-2.243-5-5-5zm-1 14h2v2h-2z"></path>
            </g>
          </svg>
        </a>
        <p class=" items-center text-s text-gray-300 ">Help</p>
      </div>
      <div class="flex flex-col items-center border-t border-gray-300">
        <a class="flex items-center justify-center w-12 h-12 m-2 "></a>
      </div>
    </div>
  );
}

export default NavBar;
