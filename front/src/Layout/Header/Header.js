import React from "react";

import logo from "../../assets/logo/logo.png";

import "./Header.css";

const Header = () => {
  return (
    <>
      <div className="addrest">
        <div className="hed">
          <div className="hed-wrapper">
            <div className="hed-wrapper-t">
              <div className="zlogo">
                <img src={logo} alt="logo" className="zlogo" />
              </div>

              <div className="pu">
                <div className="pu-i">Contact</div>
                <div className="pu-i">Login</div>
                <div className="pu-i">Signup</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Header;
