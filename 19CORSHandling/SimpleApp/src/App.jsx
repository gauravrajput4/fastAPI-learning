import React, { useState, useEffect } from 'react'
function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://localhost:8000/')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);
  return (

    <div>
      <h1>Simple React App</h1>
      {
          data ? (
              <p>
                  Message: {data.message}
              </p>)
              : (
                  <p>Loading...</p>
              )
      }
    </div>
  )
}

export default App
