import React from "react";

import logo from "../../assets/logo/logo.png";
import gplay from "../../assets/images/gplay.png";
import Astore from "../../assets/images/Astore.png";

import "./Footer.css";
const Footer = () => {
  return (
    <>
      <div className="zfot">
        <div className="zfot-wrapper">
          <div className="zfot-t">
            <div className="zfot-tlogo">
              <img src={logo} alt="" />
            </div>
          </div>
          <div className="zfot-m">
            <div className="zfotm1">
              <ul className="fotul">
                <li>
                  <h4>COMPANY</h4>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Who We Are</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Blog</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Careers</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Report Fraud</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Contact</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Inverstor Relations</p>
                  </a>
                </li>
              </ul>
            </div>

            <div className="zfotm2">
              <ul className="fotul">
                <li>
                  <h4>FOR ENTRPENEURs</h4>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Code of conduct</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Community</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Blogger Help</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Mobile Aps</p>
                  </a>
                </li>
              </ul>
            </div>

            <div className="zfotm3">
              <ul className="fotul">
                <li>
                  <h4>FOR ENTERPRISES</h4>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Zomato for Work</p>
                  </a>
                </li>
              </ul>
            </div>

            <div className="zfotm4">
              <ul className="fotul">
                <li>
                  <h4>FOR YOU</h4>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Privacy</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Terms</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Security</p>
                  </a>
                </li>
                <li>
                  <a href=" " target="_blank">
                    <p>Sitemap</p>
                  </a>
                </li>
              </ul>
            </div>

            <div className="zfotm5">
              <ul className="fotul">
                <li>
                  <h4>SOCIAL LINKS</h4>
                </li>
                <li>
                  <div className="sicons">
                    <a href=" " target="_blank" className="fa fa-facebook"></a>
                    <a
                      href="https://twitter.com/zomato"
                      target="_blank"
                      className="fa fa-twitter"
                    ></a>
                    <a
                      href="https://www.instagram.com/zomato/"
                      target="_blank"
                      className="fa fa-instagram"
                    ></a>
                    <a
                      href="https://www.youtube.com/zomato"
                      target="_blank"
                      className="fa fa-youtube"
                    ></a>
                    <a
                      href="https://in.linkedin.com/company/zomato"
                      target="_blank"
                      className="fa fa-linkedin"
                    ></a>
                  </div>
                </li>

                <li>
                  <div className="gstore">
                    <img src={gplay} alt="" />
                  </div>
                  <div className="Astore">
                    <img src={Astore} alt="" />
                  </div>
                </li>
              </ul>
            </div>
          </div>

          <div className="zfot-b">
            <p>2021-2022 © PFE-SEARCH-ENGINE™</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default Footer;
