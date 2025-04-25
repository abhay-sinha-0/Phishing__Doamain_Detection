import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputUrl, setInputUrl] = useState('');
  const [result, setResult] = useState('');

  const handleInputChange = (e) => {
    setInputUrl(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:5000/prediction', {
        inputUrl,
      });
      setResult(response.data.prediction);
    } catch (error) {
      console.error('Error fetching prediction:', error);
      setResult('Error in prediction');
    }
  };

  return (
    <div>
      <h1>URL Safety Prediction</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputUrl}
          onChange={handleInputChange}
          placeholder="Enter URL"
        />
        <button type="submit">Get Prediction</button>
      </form>
      {result && <p>{result}</p>}
    </div>
  );
}

export default App;


// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
