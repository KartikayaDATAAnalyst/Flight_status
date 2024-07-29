import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FlightStatus() {
  const [flightId, setFlightId] = useState('');
  const [status, setStatus] = useState(null);

  useEffect(() => {
    if (flightId) {
      axios.get(`/flight_status?flight_id=${flightId}`)
        .then(response => setStatus(response.data))
        .catch(error => console.error('Error fetching flight status:', error));
    }
  }, [flightId]);

  const handleChange = (event) => {
    setFlightId(event.target.value);
  };

  return (
    <div>
      <input type="text" placeholder="Enter Flight ID" value={flightId} onChange={handleChange} />
      {status && (
        <div>
          <p>Status: {status.status}</p>
          <p>Gate: {status.gate}</p>
          <p>Delay: {status.delay}</p>
        </div>
      )}
    </div>
  );
}

export default FlightStatus;
