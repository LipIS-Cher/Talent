import React from 'react';
import { Switch, Route, withRouter, BrowserRouter } from 'react-router-dom';
import './App.css';
import IndexPage from './pages/index/index.component';

class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path='/' component={IndexPage} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;
