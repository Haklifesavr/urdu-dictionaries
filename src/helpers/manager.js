import axios from 'axios';
import {
    backendRoot, 
    verifyTokenPath,
    getToken
  } from '../backendInfo';


const manager = {
    
  verifyToken: (setIsAuthenticated, logout, token, setToken) => {
    
      fetch(`${backendRoot}/${getToken}?logout=${logout}`, {
        method: "GET"
      })
      .then((res) => {
        if(res.status === 200) {
          // console.log("DEBUG TOKEN, RESPONSE", res, res.data)
          return res.json()};
      })
      .then((data) => {
        // console.log("DEBUG", data);
        setToken(data)
        if(data !== ''){
        localStorage.setItem('token', data)
      }
        localStorage.getItem('token') ? setIsAuthenticated(true) : setIsAuthenticated(false)
        // console.log('TOKEN VALUE', data, token)
      })
      .catch((error) => {
        console.log(error);
        setIsAuthenticated(false)
      });
    },

    searches: (word, dict, setCounter, setResult, setErrorMessage, setLoading) => {


      let formData = new FormData();

      formData.append("word", word);   
      formData.append("filters", JSON.stringify({"dic": dict}));
      
        fetch(`${backendRoot}/dict_api/search/`, {
            method: "POST",
            headers: {
              Accept: "application/json",
            },
            body: formData,
          })
          .then((res) => {
            if (res.ok) return res.json()
              
          })
          .then((data) => {
            // console.log("DEBUG :SEARCH DOCS API CALL...", data, typeof(data));
            data === undefined ? setErrorMessage('Result not found') : setResult(data)
            setLoading(false)
            setCounter(0)
          })
          .catch((error) => {
            console.log(error);
          });

      },

    translation: (selectedRadiobtn, word, setResult, setErrorMessage, setLoading) => {

      fetch(`${backendRoot}/oxford_api/synonyms/?word=${word}&target_lang=${selectedRadiobtn}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json"
          },
        })
        .then((res) => {
          if (res.ok) return res.json();
        })
        .then((data) => {
          // console.log("DEBUG :TRANSLATE DOCS API CALL", data, typeof(data));
          data === undefined ? setErrorMessage('Translation not found') : setResult(data)
          setLoading(false)
        })
        .catch((error) => {
          console.log(error);
        });
      }
};

export default manager;