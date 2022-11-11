import React, { useRef, useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

import "./Filter.css";

const Filter = () => {
  const [skills, setSkills] = useState("");
  const [company, setCompany] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");
  const [phone, setPhone] = useState("");

  const form = useRef();

  const subimtHandler = (e) => {
    e.preventDefault();

    setSkills("");
    setCompany("");
    setSubject("");
    setMessage("");
    setPhone("");
  };

  return (
    <>
      <div className="filter_card">
        <form ref={form} onSubmit={subimtHandler}>
          <div className="row filter_label">
            <div className="col-6 label_filter">
              <h5>filter by skills</h5>
            </div>

            <div className="col-6 ">
              <TextField
                id="filled-basic"
                value={skills}
                onChange={(e) => setSkills(e.target.value)}
                label="skills"
                variant="filled"
              />
            </div>
          </div>

          <div className="row filter_label">
            <div className="col-6 label_filter">
              <h5>filter by company name</h5>
            </div>

            <div className="col-6">
              <TextField
                id="filled-basic"
                value={company}
                onChange={(e) => setCompany(e.target.value)}
                label="company name"
                variant="filled"
              />
            </div>
          </div>

          <div className="row filter_label">
            <div className="col-6 label_filter">
              <h5>filter by company name</h5>
            </div>

            <div className="col-6">
              <TextField
                id="filled-basic"
                label="company name"
                variant="filled"
              />
            </div>
          </div>
          <Button type="submit" className="theme-btn" variant="contained">
            Search
          </Button>
        </form>
      </div>
    </>
  );
};

export default Filter;
