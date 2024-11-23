
import './App.css';
import React from "react";

function App() {
  const divRef = React.useRef(null);
  const [value, setValue] = React.useState("");

  return (
    <div className="App">
      <header className="App-header">
        <h1>XSS Vulnerability</h1>
        <p>by Igor Mpore</p>
      </header>
      <div className='formWrapper'>
        <div className='form'>
          <input type="text" placeholder='Your name' />
          <textarea value={value} onChange={(e) => setValue(e.target.value)} cols="30" rows="10" placeholder='Type your Message to print'></textarea>
          <button onClick={() => {
            divRef.current.innerHTML = value;
          }}>Submit</button>
        </div>
      </div>
      <div ref={divRef} className='notifyWrapper'>
      </div>
    </div>
  );
}

export default App;