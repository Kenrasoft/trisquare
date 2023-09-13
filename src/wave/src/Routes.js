// src/Routes.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SectorsTable from './components/SectorsTable';

const Routes = () => {
  return (
    <Router>
      <Switch>
        <Route path="/sectors" component={SectorsTable} />
        {/* Add more routes as needed */}
      </Switch>
    </Router>
  );
};

export default Routes;
