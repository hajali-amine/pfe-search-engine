import React, { useRef, useState } from "react";

import Footer from "../../Layout/Footer/Footer";
import Header from "../../Layout/Header/Header";

import "./Home.css";
import CompanyCard from "./Components/CompanyCard/CompanyCard";
import Search from "./Components/Search/Search";
import Filter from "./Components/Filter/Filter";
import Button from "@mui/material/Button";
import apiService from "../../api/apiService";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";

import { BsBuilding } from "react-icons/bs";
import { MdTitle, MdLocationOn } from "react-icons/md";
import { GiSkills } from "react-icons/gi";
import FormControl from "@mui/material/FormControl";

const Home = () => {
  const [data, setData] = useState([]);
  const [input, setInput] = useState("");
  const [filtertype, setFilterType] = useState("location");

  const form = useRef();

  const handleChange = (event) => {
    setFilterType(event.target.value);
  };
  const subimtHandler = (e) => {
    e.preventDefault();

    console.log(filtertype);

    apiService
      .getdata(filtertype, input)
      .then((response) => {
        setData(response.data);
        console.log(response);
      })
      .catch((e) => {
        console.log(e);
      });
  };
  return (
    <>
      <Header />

      <div className="header max-width">
        <div className="header-right">
          <div className="header-location-search-container">
            <div className="location-wrapper">
              <div className="location-icon-name">
                <FormControl sx={{ m: 1, minWidth: 120 }}>
                  <Select
                    value={filtertype}
                    onChange={handleChange}
                    displayEmpty
                    inputProps={{ "aria-label": "Without label" }}
                    className="dropdown_select"
                  >
                    <MenuItem value="location">
                      <MdLocationOn
                        style={{ fontSize: "1.5em", color: "#d75809" }}
                        className="iconify"
                      />
                      <div>Location</div>
                    </MenuItem>

                    <MenuItem value={"company"}>
                      <BsBuilding
                        style={{ fontSize: "1.5em", color: "#d75809" }}
                        className="iconify"
                      />
                      Company
                    </MenuItem>
                    <MenuItem value="internship">
                      <MdTitle
                        style={{ fontSize: "1.5em", color: "#d75809" }}
                        className="iconify"
                      />
                      Title
                    </MenuItem>
                    <MenuItem value="skill">
                      <GiSkills
                        style={{ fontSize: "1.5em", color: "#d75809" }}
                        className="iconify"
                      />
                      Skill
                    </MenuItem>
                  </Select>
                </FormControl>
              </div>
              <i className="fi fi-rr-caret-down absolute-center"></i>
            </div>
            <div className="location-search-separator"></div>
            <div className="header-searchBar">
              <form ref={form} onSubmit={subimtHandler}>
                <input
                  className="search-input"
                  placeholder="Search for  an opportunity "
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                />

                <Button type="submit" className="theme-btn" variant="contained">
                  {" "}
                  <span
                    style={{ fontSize: "2em" }}
                    className="iconify"
                    data-icon="ei:search"
                  ></span>
                </Button>
              </form>
            </div>
          </div>
        </div>
      </div>

      <div className="row main_home">
        <div className="col-1"></div>

        <div className="col-10">
          {data.map((item, index) => (
            <CompanyCard key={index} item={item[0]} />
          ))}
        </div>

        <div className="col-1"></div>
      </div>
      <Footer />
    </>
  );
};

export default Home;
