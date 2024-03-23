import './App.css';
import MatrixBackground from './background/background';

function App() {
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
    <div className="minfosec">
      <label className='mnlbl'>Machine Name turn this into a variable</label>
      <div className='minfo'>
      <label className='infolbl'>MAC Address: </label>
        <label className='infolbl'>Default Gateway: </label>
        <label className='infolbl'>Local Address: </label>
      </div>
    </div>
  </div>
  </div>
 </div>
  );
}

export default App;
