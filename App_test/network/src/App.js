import './App.css';
import React, {useState, useEffect} from 'react';
import MatrixBackground from './background/background';
import Minfotile from './minfotiles/minfotiles';

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://localhost:5000/mdata").then(
        res => res.json()
    ).then(
      data => {
        setData(data)
      }
    )
  }, [])
  

  return (
 <div id="Network">
    <MatrixBackground/>
    <div id="body">
      <div id="Header">
        <label id="Title">
          Network Info Test
        </label>
      </div>
      <div id="Content">
        {data.map(item => (
          <Minfotile data={item}/>
        ))}
      </div>
    </div>
  </div>
  );
}

export default App;
