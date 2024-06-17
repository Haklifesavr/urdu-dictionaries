import React, {  useState, useContext} from 'react';


const AppContext= React.createContext({
    state:{},
    actions:{}
})

const propTypes = {
};

const defaultProps = {
};


function AppProvider(props){


    const [translate, setTranslate] = useState("");
    const [operation, setOperation] = useState("");
    const [token,setToken] = useState("")
    const [result, setResult] = useState("");
    const [result2, setResult2] = useState("");
    const [loading, setLoading] = useState(false);
    const [filters, setFilters] = useState({});
    const [counter, setCounter] = useState(0);
    const [errorMessage,setErrorMessage]=useState(null);
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const [logout, setLogout] = useState(0)


    const state={
        translate,
        operation,
        result,
        result2,
        loading,
        filters,
        counter,
        errorMessage,
        isAuthenticated,
        logout,
        token
    }
    const actions={
        setTranslate,
        setOperation,
        setResult,
        setResult2,
        setLoading,
        setFilters,
        setCounter,
        setErrorMessage,
        setIsAuthenticated,
        setLogout,
        setToken
    }


    return (
        <AppContext.Provider value={{state,actions}}>
            {props.children}
        </AppContext.Provider>
    )
}

AppProvider.propTypes = propTypes;
AppProvider.defaultProps = defaultProps;

function useApp(props){
    return useContext(AppContext)
}

export {
    AppProvider,
    useApp,
}

