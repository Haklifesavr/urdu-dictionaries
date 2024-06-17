import React, { useState, useEffect } from "react";
import { Box } from "@mui/material";
import Button from "@mui/joy/Button";
import { useApp } from "../../AppContext";
import manager from "../../helpers/manager";

export default function SearchButtons(props) {
  const ceo = useApp();

  useEffect(() => {
    ceo.actions.setOperation("")
    if(ceo.state.result !== ""){
    ceo.actions.setLoading(false)
  }
    // console.log("TRANSLATION RESULT",ceo.state.result)
  },[ceo.state.result]);

  useEffect(() => {
    if(ceo.state.operation !== "" && ceo.state.translate !== ""){
    ceo.actions.setResult("")
    ceo.actions.setLoading(true)
    }
    if(ceo.state.translate !== ""){
    if (ceo.state.operation === "de") {
      // console.log("TRANSLATE STATE INSIDE GERMAN_BTN", ceo.state.translate);
      manager.translation(ceo.state.operation, ceo.state.translate, ceo.actions.setResult, ceo.actions.setErrorMessage, ceo.actions.setLoading)
    }

    if (ceo.state.operation === "fr") {
      // console.log("TRANSLATE STATE INSIDE FRENCH_BTN", ceo.state.translate);
      manager.translation(ceo.state.operation, ceo.state.translate, ceo.actions.setResult, ceo.actions.setErrorMessage, ceo.actions.setLoading);
    }
    if (ceo.state.operation === "es") {
      // console.log("TRANSLATE STATE INSIDE SPANISH_BTN", ceo.state.translate);
      manager.translation(ceo.state.operation, ceo.state.translate, ceo.actions.setResult, ceo.actions.setErrorMessage, ceo.actions.setLoading);
    }
  }
  }, [ceo.state.operation]);

  const GermanHandler = (e) => {
    e.preventDefault();
    ceo.actions.setResult("")
    ceo.actions.setResult2("")
    ceo.actions.setLoading(true)
    ceo.actions.setOperation("de");
    props.formHandler(e);
    // console.log("TRANSLATE STATE INSIDE GERMAN HANDLER", ceo.state.translate);
  };
  const FrenchHandler = (e) => {
    e.preventDefault();
    ceo.actions.setResult("")
    ceo.actions.setResult2("")
    ceo.actions.setLoading(true)
    ceo.actions.setOperation("fr");
    props.formHandler(e);
    // console.log("TRANSLATE STATE INSIDE FRENCH HANDLER", ceo.state.translate);
  };
  const SpanishHandler = (e) => {
    e.preventDefault();
    ceo.actions.setResult("")
    ceo.actions.setResult2("")
    ceo.actions.setLoading(true)
    ceo.actions.setOperation("es");
    props.formHandler(e);
    // console.log("TRANSLATE STATE INSIDE SPANISH HANDLER", ceo.state.translate);
  };
  return (
    <>
      <Box
        style={{
          display: "flex",
          gap: 15,
        }}
      >
        <Box>
          <Button
            id="german_btn"
            onClick={GermanHandler}
            variant="contained"
            sx={{ bgcolor: "#2a9ab4" }}
          >
            Translate to German
          </Button>
        </Box>
        <Box>
          <Button
            id="french_btn"
            onClick={FrenchHandler}
            variant="contained"
            sx={{ bgcolor: "#2a9ab4" }}
          >
            Translate to French
          </Button>
        </Box>

        <Box>
          <Button
            id="spanish_btn"
            onClick={SpanishHandler}
            variant="contained"
            sx={{ bgcolor: "#2a9ab4" }}
          >
            Translate to Spanish
          </Button>
        </Box>
      </Box>
    </>
  );
}
