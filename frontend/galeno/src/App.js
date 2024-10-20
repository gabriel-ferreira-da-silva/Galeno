import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import FormPage from './pages/FormPage';
import { Galnavbar } from './components/navbar/Galnavbar';
function App() {
  return (
    <div>
      <Galnavbar></Galnavbar>
      <Router>
        <Routes>
        <Route path="/" element={<FormPage/>}/>
        <Route path="/predict" element={<FormPage/>}/>
        </Routes>
      </Router>
    </div>

  );
}

export default App;
