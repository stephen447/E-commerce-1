import React, { Component } from "react"
import {BrowserRouter as Router, Route, Routes, Link} from "react-router-dom"
import { Grid, Button, ButtonGroup, Typography } from "@mui/material";
import Login from "./login";


export default class HomePage extends Component{
    constructor(props) {
      super(props);
      
    }

    renderHomePage() {
      return (
            <p>Home page placeholder</p>
        )
    }
    
    render(){
        return(
        <Router>
            <Routes>
                <Route path="" element = {this.renderHomePage()}/>
                <Route path="login" element = {<Login/>}/>
            </Routes>
        </Router>)
    }
}


