import React, { useState, useEffect, useRef } from "react";
import { Grid, Box, Typography, Paper } from "@mui/material";
import { useApp } from "../../AppContext";

const ResultSearch = (props) => {
     const ceo = useApp();
     const ref = useRef(null);
     useEffect(() => {
          ref.current?.scrollIntoView({behavior: 'smooth'});
        },[ceo.state.result2]);


     return (
        <>
        {ceo.state.result2.map((res) => {
            return(
              <React.Fragment key={res.dictionary}>
            <Paper ref={ref} elevation={4} sx={{p:5, mb:3, mt:1}}>
            <Typography sx={{color: "#17a2b8", fontSize: "25px", fontWeight: "bold", mb:1.5}}>
                {ceo.state.translate.replace(/\b\w/g, function (l) {
                  return l.toUpperCase();
                })}
                </Typography>
            <Typography sx={{color: "#17a2b8", mb:1.5}}>{res.dictionary}</Typography>
            <Box sx={{display: "flex", gap:2}}>
            <Typography sx={{color: "#17a2b8", fontSize: "15px", mb:1.5}}>Words:</Typography>
            <Box sx={{display: "flex", gap:2, mb:1.5}}>
            {res.word.length > 0 &&
            res.word.map((words, index) => {
                return(
                  <React.Fragment key={index}>
                    {res.lang === "en" ? 
                    <Typography sx={{fontSize: "15px"}}>{words}{res.word.length-1 ? ",": ""}</Typography>
                  : 
                  <Typography sx={{fontSize: "15px", fontFamily: "NotoNastaliqUrdu-Regular"}}>{index === 0 ? "": "،"}{words}</Typography>
                } 
                </React.Fragment>
                )
            })
            }
            </Box>
            </Box>
            <Box sx={{display: "flex", gap:2}}>
            <Typography sx={{color: "#17a2b8", fontSize: "15px", mb:1.5}}>Meanings:</Typography>
            <Box sx={{display: "flex", gap:2, mb:1.5}}>
            {res.meanings.length > 0 &&
            res.meanings.map((words, index) => {
                return(
                  <React.Fragment key={index}>
                    {res.lang === "ur" ? 
                    <Typography sx={{fontSize: "15px"}}>{words}{res.meanings.length-2 ? ",": ""}</Typography>
                  : 
                  <Typography sx={{fontSize: "15px", fontFamily: "NotoNastaliqUrdu-Regular"}}>{index === 0 ? "": "،"}{words}</Typography>
                } 
                </React.Fragment>
                )
            })
            }
            </Box>
            </Box>
            </Paper>
            </React.Fragment>
            )
        })}
        </>
     );
   
};

export default ResultSearch;
