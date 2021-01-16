import React from 'react';
import './App.css';
import Header from './components/Header'
import Main from './components/Main'
import Login from './components/Login'
import {Route, BrowserRouter as Router} from "react-router-dom"
// '''
// you can have inline styles, you can also create style objects and pass that to the style
// property of a html tag <h1 style={styles}>
// '''

class App extends React.Component{
  render(){
    return (
      <Router>
      <div>
        <Header />
      </div>
      <Route path='/' exact component={Login}/ >
      <Route path='/Main/:access_token'> <Main /> </Route>
      </Router>

    );
  }
}


export default App;
