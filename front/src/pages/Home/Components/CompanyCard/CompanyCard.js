import React from "react";

import comanyLogo from "../../../../assets/images/company-enterprise.webp";

import "./CompanyCard.css";

const CompanyCard = ({ item }) => {
  return (
    <>
      <div className="company_card">
        <div className="col-4 company_image whyp-b-icon">
          <img src={comanyLogo} alt="globe" />
        </div>

        <div className="col-8">
          <div className="why-b-crd">
            <h3>{item.internship}</h3>
            <h4>{item.company}</h4>
            <p>{item.location}</p>
            <p>{item.description}</p>
            <h6>skills:</h6>
            <p>{item.skills.map((item) => item + ",")}</p>

            <a href={item.link} target="_blankv" className="apply_btn">
              {" "}
              apply
            </a>
          </div>
        </div>
      </div>
    </>
  );
};

export default CompanyCard;
