import { Snackbar } from "@mui/material";
import React, {useState,useEffect} from "react";




export default function CustomSnackbar(props){
    const [open,setOpen]=useState(false);


    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
          return;
        }
        setOpen(false);
      };
    useEffect(()=>{
        if (props.message){
            setOpen(true);
            setTimeout(()=>{ console.log("RUNNING TIMEOUT");props.setMessage(null)},3100)
        }
    },[props.message])
    return (
        props.message ? (
        <Snackbar
				open={open}
				autoHideDuration={3000}
				onClose={handleClose}
				message={props.message}
				action={null}
        sx={props.snack_styles}
				anchorOrigin={{vertical:'bottom',horizontal:'center'}}
			/>
        ): null
    )
} 