import React, { useState, useEffect, useRef } from "react";
import { Grid, InputAdornment, Typography, Box } from "@mui/material";
import TextField from "@mui/joy/TextField";
import { Input, FormControl, FormLabel } from "@mui/joy";
import Button from "@mui/joy/Button";
import logo from "../assets/Dictionaries Logo.png";
import ResultTranslate from "../ResultTranslate/ResultTranslate";
import ResultSearch from "../ResultSearch/ResultSearch";
import { useApp } from "../../AppContext";
import SearchButtons from "../SearchButtons/SearchButtons";
import SearchFilters from "../SearchFilters/SearchFilters";
import CircularProgress from '@mui/material/CircularProgress';
import Cookie from 'universal-cookie';
import manager from '../../helpers/manager';

function Search() {
  const ceo = useApp();

  useEffect(() => {
    if(ceo.state.translate !== ""){
      ceo.actions.setLoading(true)
    }
    if(ceo.state.translate === "" || ceo.state.counter === 0){
      ceo.actions.setLoading(false)
    }
    // console.log("TRANSLATE AND COUNTER STATE INSIDE USE EFFECT", ceo.state.translate, ceo.state.counter);
  }, [ceo.state.translate, ceo.state.counter]);

  const verifyLogin = () => {
    // console.log("DEBUG TEMP", localStorage.getItem('token'));
    localStorage.getItem('token') ? ceo.actions.setIsAuthenticated(true) : ceo.actions.setIsAuthenticated(false)
}

const logOut = (e) => {
  e.preventDefault();
  localStorage.removeItem('token')
  verifyLogin()
  ceo.actions.setLogout(1)
  manager.verifyToken(ceo.actions.setIsAuthenticated, 1, ceo.state.token, ceo.actions.setToken)
  verifyLogin()
}

  const searchClick = (e) => {
    e.preventDefault();
    ceo.actions.setResult("")
    ceo.actions.setResult2("")
    ceo.actions.setCounter(Math.random())
    handleSearchSubmit(e)
    // console.log("COUNTER STATE", ceo.state.counter)
  }

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    const tmp = document.getElementById("input-value").value;
    if (tmp !== ""){
    ceo.actions.setTranslate(tmp);
  }
  else{
    ceo.actions.setErrorMessage("Nothing to Search or Translate")
    ceo.actions.setTranslate("")
  }
    // console.log("TRANSLATE STATE INSIDE SEARCH SUBMIT", ceo.state.translate, tmp);
  };
  return (
    <>
    <Grid container sx={{m:2}} direction="column" alignItems="flex-start">
      <Button onClick = {logOut} sx={{ bgcolor: "#2a9ab4"}} variant = "contained">Log Out</Button>
      </Grid>
    <Grid
      sx={{ mt: 1 }}
      container
      spacing={0}
      direction="column"
      alignItems="center"
      justifyContent="center"
    >
      <Grid item xs={3}>
        <img src={logo} alt="Logo" />
      </Grid>
      <Grid item xs={3}>
        <Typography
          component="h1"
          fontWeight="xl"
          sx={{
            color: "#17a2b8",
            fontFamily: "NotoNastaliqUrdu-Regular",
            fontSize: "30px",
            mt: 2,
            mb: 2,
          }}
        >
          اُردو لُغت
        </Typography>
      </Grid>
      <Grid item xs={3}>
      <FormControl>
  <FormLabel>...</FormLabel>
  <Input 
  id="input-value"
  size="lg"
  placeholder="Search"
  // }
  sx={{
    maxWidth: "55vw",
    minWidth: "40vw",
    border: "5px solid #2a9ab4",
  }}
  /> {/* This could be Textarea, Select, Autocomplete */}
</FormControl>
          {/* <TextField
            id="input-value"
            size="lg"
            placeholder="Search"
            // }
            sx={{
              maxWidth: "55vw",
              minWidth: "40vw",
              border: "5px solid #2a9ab4",
              // borderRadius: "13px",
            }}
          /> */}
      </Grid>
      <Grid item xs={3} sx={{ mt: 2 }}>
        <SearchFilters />
      </Grid>
      <Grid item xs={3} sx={{ mt: 2 }}>
        <SearchButtons formHandler={handleSearchSubmit} />
      </Grid>
      <Grid item xs={3} sx={{ mt: 2.5 }}>
          <Button 
            onClick={searchClick}  
            sx={{
              width: "10vw",
              color: "#2a9ab4",
              border: "2px solid #2a9ab4",
              // borderRadius: 8,
            }}
            variant="outlined"
            // lg
          >
            Search
          </Button>
      </Grid>
      <Grid item xs={3} sx={{ mt: 2 }}>
        {ceo.state.result !== "" ? <ResultTranslate /> : ceo.state.result2 !== "" ? <ResultSearch /> : ceo.state.loading ? <CircularProgress sx={{color: "#17a2b8"}} /> : null}
      </Grid>
    </Grid>
    </>
  );
}

export default Search;
