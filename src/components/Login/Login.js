import "./Login.css";
import * as React from "react";
import Avatar from "@mui/joy/Avatar";
import micon from "../../icons/microsoft/microsoft.png";
import gicon from "../../icons/google/google.png";
import Button from "@mui/joy/Button";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { backendRoot } from '../../backendInfo';

function Login() {
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
  };

  return (
    <div className="container">
        
      <div className="text-center">
        <h1 className="heading"> اُ ردو لغت </h1>{" "}
      </div>
        <div className="login-main">
          <Container
            component="main"
            maxWidth="xs"
            className="login-component-outer"
          >
            <Box className="bigbox">
              <Avatar sx={{ m: 1, mb: 3, bgcolor: "#17a2b8", color:"#fff" }}>
                <LockOutlinedIcon />
              </Avatar>{" "}

              <Typography className="welcome">Hey, Welcome Back!</Typography>
              <Box sx={{ mt: 1 }}>
                <div className="buttonDiv">
                  <Button
                    type="submit"
                    className="microsoft-button"
                    href={`${backendRoot}/accounts/microsoft/login/`}
                    variant="outlined"
                  >
                    <img src={micon} className="icon"></img>
                    Microsoft Sign In{" "}
                  </Button>{" "}
                </div>

                <div className="buttonDiv2">
                <Button
  type="submit"
  className="google-button"
  variant="outlined"
  onClick={() => window.location.href=`${backendRoot}/accounts/google/login/?process=login`}
>
  <img src={gicon} className="icon"></img>
  Google Sign In
</Button>
{" "}
                </div>
              </Box>{" "}
            </Box>{" "}
          </Container>{" "}
        </div>{" "}
    </div>
  );
}

export default Login;
