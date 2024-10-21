import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import FormPage from './pages/FormPage';
import { Galnavbar } from './components/navbar/Galnavbar';
import InfoPage from './pages/InfoPage';
function App() {
  return (
    <div>
      
      <Router>
        <Galnavbar></Galnavbar>
        <Routes>
        <Route path="/" element={<FormPage/>}/>
        <Route path="/predict" element={<FormPage/>}/>
        <Route path="/info" element={<InfoPage/>}/>
        </Routes>
      </Router>
    </div>

  );
}

export default App;
