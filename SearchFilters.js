import React, { useState, useEffect, useRef } from "react";
import OutlinedInput from "@mui/material/OutlinedInput";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Box from "@mui/material/Box";
import FormControl from "@mui/material/FormControl";
import ListItemText from "@mui/material/ListItemText";
import Select from "@mui/material/Select";
import Checkbox from "@mui/material/Checkbox";
import { useApp } from "../../AppContext";
import manager from "../../helpers/manager";

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
};

const names = [
  "None",
  "Al Mawrid: Arabic-English Dictionary",
  "Hayyim, Sulayman. New Persian-English dictionary",
  "Steingass, Francis Joseph. A Comprehensive Persian-English dictionary",
  "English-to-Urdu Standard",
  "Urdu to English Standard",
  "Urdu Inc",
  "Urdu Idioms",
  "Urdu Lughat Tarikhi Asool Par",
  "S. W. Fallon's 'A new Hindustani-English dictionary'",
  "Kitabistan's 20th-Century Standard Dictionary: Urdu Into English",
  "Platts, John T. (John Thompson). A dictionary of Urdu, classical Hindi, and English. London: W. H. Allen & Co., 1884",
  "John Shakespear’s",
  "oxford",
  "Google",
  "Urdu Seek",
  "Lanes Lexicon",
  "Hans Wehr Dictionary",
];

export default function MultipleSelectCheckmarks() {
  const ceo = useApp();
  const [dictName, setDictName] = React.useState([]);
  const [open, setOpen] = React.useState(false);

  useEffect(() => {
    ceo.state.filters['0'] = names.slice(1)
    ceo.state.filters['1'] = false 
    console.log("DATA IN FILTER USEEFFECT",ceo.state.filters)
    },[]);

    useEffect(() => {
      if(ceo.state.result2 !== ""){
      ceo.actions.setLoading(false)
      }
      // console.log("SEARCH RESULT",ceo.state.result2)
    },[ceo.state.result2]);

  useEffect(() => {
    if(ceo.state.counter !== 0 && ceo.state.translate !== ""){
      manager.searches(ceo.state.translate, ceo.state.filters, ceo.actions.setCounter, ceo.actions.setResult2)
    } 
  },[ceo.state.counter]);

  const handleClose = () => {
    setOpen(false);
  };

  const handleOpen = () => {
    setOpen(true);
  };

  const handleChange = (event) => {
    const {
      target: { value },
    } = event;
    console.log("FILTERED VALUE", value);
    if (value.includes("None")) {
      setDictName([]);
      ceo.state.filters['0'] = names.slice(1)
      ceo.state.filters['1'] = false
      // ceo.actions.setFilters({});
    } else {
      setDictName(
        // On autofill we get a stringified value.
        typeof value === "string" ? value.split(",") : value
      );
      ceo.state.filters['0'] = typeof value === "string" ? value.split(",") : value
      ceo.state.filters['1'] = false
    }
    setOpen(false);
    console.log("DATA IN FILTER",ceo.state.filters)
  };

  return (
    <Box
      style={{
        display: "flex",
      }}
    >
      <FormControl sx={{ m: 1, width: "24vw" }}>
        <InputLabel id="demo-controlled-open-select-label">Filters</InputLabel>
        <Select
          labelId="demo-controlled-open-select-label"
          id="demo-controlled-open-select"
          open={open}
          onClose={handleClose}
          onOpen={handleOpen}
          multiple
          value={dictName}
          onChange={handleChange}
          input={<OutlinedInput label="Filters" />}
          renderValue={(selected) => selected.join(", ")}
          MenuProps={MenuProps}
        >
          {names.map((name) => (
            <MenuItem key={name} value={name}>
              <Checkbox checked={dictName.indexOf(name) > -1} />
              <ListItemText primary={name} />
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
}
