import React, { useState, useEffect, useRef } from "react";
import { Grid, Box, Typography, Paper } from "@mui/material";
import { useApp } from "../../AppContext";

const ResultTranslate = (props) => {
     const ceo = useApp();
     const ref = useRef(null);
     useEffect(() => {
          ref.current?.scrollIntoView({behavior: 'smooth'});
     },[ceo.state.result]);

     const translation = ceo.state.result[0];
     const res = ceo.state.result[1];

     return (
     <>
               <Paper ref={ref} elevation={4} sx={{p:5, mb:3, mt:1}}>
               <Typography sx={{color: "#17a2b8", fontSize: "25px", fontWeight: "bold", mb:1.5}}>
               {ceo.state.translate.replace(/\b\w/g, function (l) {
                    return l.toUpperCase();
               })} ({translation['translation']})
               </Typography>
               <Typography sx={{color: "#17a2b8", mb:1.5}}>{res.dictionary}</Typography>
               <Box sx={{display: "flex", gap:2}}>
               <Typography sx={{color: "#17a2b8", fontSize: "15px", mb:1.5}}>Synonyms:</Typography>
               <Box sx={{display: "flex", gap:2, mb:1.5}}>
               {res.synonyms.length > 0 &&
               res.synonyms.map((words, index) => {
                    return(
                         <React.Fragment key={index}>
                    <Typography sx={{fontSize: "15px"}}>{words}{index < res.synonyms.length-2 ? ",": ""}</Typography>
                    </React.Fragment>
                    )
               })
               }
               </Box>
               </Box>
               <Box sx={{display: "flex", gap:2}}>
               <Typography sx={{color: "#17a2b8", fontSize: "15px"}}>Translation:</Typography>
               <Box sx={{display: "flex", gap:2}}>
               {res.meanings.length > 0 &&
               res.meanings.map((words, index) => {
                    return(
                         <React.Fragment key={index}>
                         <Typography sx={{fontSize: "15px"}}>{words}{index < res.meanings.length-2 ? ",": ""}</Typography>
                         </React.Fragment>
                    )
               })
               }
               </Box>
               </Box>
               </Paper>
     </>
          );

};

export default ResultTranslate;
