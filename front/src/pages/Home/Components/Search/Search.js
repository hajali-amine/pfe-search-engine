import React, { useRef, useState } from "react";
import Button from "@mui/material/Button";
import MenuItem from "@mui/material/MenuItem";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";

import "./Search.css";
const Search = ({ setData }) => {
  const [input, setInput] = useState();
  const [filtertype, setFilterType] = useState();

  const form = useRef();

  const subimtHandler = (e) => {
    e.preventDefault();
    console.log(filtertype);
    setData([]);
  };
  return (
    <>
      <div className="header max-width">
        <div className="header-right">
          <div className="header-location-search-container">
            <div className="location-wrapper">
              <div className="location-icon-name">
                <FormControl sx={{ m: 1, minWidth: 120 }}>
                  <Select
                    value={filtertype}
                    onChange={setFilterType}
                    displayEmpty
                    inputProps={{ "aria-label": "Without label" }}
                  >
                    <MenuItem value="">
                      <em>None</em>
                    </MenuItem>
                    <MenuItem value={10}>Ten</MenuItem>
                    <MenuItem value={20}>Twenty</MenuItem>
                    <MenuItem value={30}>Thirty</MenuItem>
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
                  placeholder="Search for an opportunity "
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
    </>
  );
};

export default Search;
