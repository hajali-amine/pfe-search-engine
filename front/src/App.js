import React from "react";

import { Route, Routes } from "react-router";
import PageNotFound from "./pages/PageNotFound/PageNotFound";
import Home from "./pages/Home/Home";

const App = () => {
  return (
    <>
      <Routes>
        <Route exact to path={"/"} element={<Home />} />
        <Route path={"*"} element={<PageNotFound />} />
      </Routes>
    </>
  );
};

export default App;
