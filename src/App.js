import React, { useEffect, useState } from "react";
import Search from "./components/Search/Search";
import Cookies from "js-cookie";
import Login from "./components/Login/Login";
import "./App.css";
import "./index.css";
import icon from './icons/icon/book-32.ico';
import CustomSnackbar from "./components/SnackBar/SnackBar"
import Auth from "./components/Auth/Auth"
import { useApp } from "./AppContext";

function App() {
    const ceo = useApp();
        return ( <div >
            <Auth>
            <link rel="icon" href={icon} />
            <Search />
            <CustomSnackbar
                message={ceo.state.errorMessage}
                setMessage={ceo.actions.setErrorMessage}
              />
              </Auth>
            </div>);
    }

    export default App;