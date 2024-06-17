import React, { useEffect } from 'react'
import icon from '../../icons/icon/book-32.ico';
import manager from '../../helpers/manager';
import Login from '../Login/Login';
import { useApp } from "../../AppContext";


const Auth = (props) => {
  const ceo = useApp();

  useEffect(() => {
    ceo.actions.setLogout(0)
    ceo.actions.setToken('')
    manager.verifyToken(ceo.actions.setIsAuthenticated, ceo.state.logout, ceo.state.token, ceo.actions.setToken)
    verifyLogin()
  }, [])

  useEffect(() => {
    manager.verifyToken(ceo.actions.setIsAuthenticated, ceo.state.logout, ceo.state.token, ceo.actions.setToken)
  }, [ceo.state.token])

  const verifyLogin = () => {
    // console.log("DEBUG TEMP", localStorage.getItem('token'));
    localStorage.getItem('token') ? ceo.actions.setIsAuthenticated(true) : ceo.actions.setIsAuthenticated(false)
}

  // console.log('Auth status: ', ceo.state.isAuthenticated)
  return ceo.state.isAuthenticated ? props.children: <div><link rel="icon" href={icon} /><Login /></div>

}


export default Auth;