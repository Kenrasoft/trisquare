// src/components/SectorsTable.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function SectorsTable() {
  const [sectors, setSectors] = useState([]);

  useEffect(() => {
    // Define your Flask API endpoint
    const apiUrl = 'http://localhost:5000/sectors';

    // Make a GET request to the API
    axios.get(apiUrl)
      .then(response => {
        // Update the state with the received data
        setSectors(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []); // Empty dependency array ensures this runs once on component mount

  return (
    <div>
      <h2>Sectors</h2>
      <table>
        <thead>
          <tr>
            <th>Sector</th>
          </tr>
        </thead>
        <tbody>
          {sectors.map(sector => (
            <tr key={sector.sector}>
              <td>{sector.sector}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default SectorsTable;
