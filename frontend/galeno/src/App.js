import './App.css';
import FormPage from './pages/FormPage';
import InfoPage from './pages/InfoPage';
import AddModelPage from './pages/AddModelPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Galnavbar } from './components/navbar/Galnavbar';
function App() {
  return (
    <div>
      
      <Router>
        <Galnavbar></Galnavbar>
        <Routes>
        <Route path="/" element={<FormPage/>}/>
        <Route path="/predict" element={<FormPage/>}/>
        <Route path="/addmodel" element={<AddModelPage/>}/>
        <Route path="/info" element={<InfoPage/>}/>
        </Routes>
      </Router>
    </div>

  );
}

export default App;
