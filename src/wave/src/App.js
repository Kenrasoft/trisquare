import React from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Sectors from './pages/Sectors';
import SectorsMarketCap from './pages/SectorsMarketCap';
import HistoricalData from './components/HistoricalData';
import CompareMarketCap from './pages/CompareMarketCap';
import Localbase from "localbase";
import axios from "axios";
import { apiRepo } from './context/apiConfig';

let pangea_loaded = false;

function App() {

  fetchPangeaData();
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sectors" element={<Sectors />} />
        <Route path="/sectors-marketcap" element={<SectorsMarketCap />} />
        <Route path="/historical-marketcap" element={<HistoricalData />} />
        <Route path="/compare-marketcap" element={<CompareMarketCap />} />
      </Routes>
    </Router>
  );
}

async function fetchPangeaData() {
  try {
    if (!pangea_loaded && apiRepo.type === "edge") {

      const response = await axios.get('pangea_edge.json');
      console.log("Fetching data..DONE");
      resetPangeaEdge(response.data);
    }
  } catch (error) {
    console.log("Error loading Pangea", error);
  } finally {

  }
};


function resetPangeaEdge(data) {
  const db = new Localbase('pangea');
  db.config.debug = false;

  if (!pangea_loaded) {
    db.delete().then(() => {
      console.log('Pangea is reset to the initial state.');
      loadPangeaEdge(db, data);
    });
  }

}
function loadPangeaEdge(db, data) {

  for (const key in data) {
    const records = data[key];
    if (Array.isArray(records)) {

      records.forEach(record => {
        db.collection(key).add(record);
        console.log(`${key} is loaded to Pangea.`);
      });
    }
    else if (typeof records === 'object' && records !== null) {
      db.collection(key).add(records);
      console.log(`${key} is loaded to Pangea.`);
    }
  }

  console.log('Pangea loading is DONE.');
  pangea_loaded = true;

}


export default App;
