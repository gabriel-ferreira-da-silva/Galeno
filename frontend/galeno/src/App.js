import './App.css';
import FormPage from './pages/FormPage';
import InfoPage from './pages/InfoPage';
import AddModelPage from './pages/AddModelPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Galnavbar } from './components/navbar/Galnavbar';
import TrainModelPage from './pages/TrainModelPage';
import { Sidebar } from 'react-pro-sidebar';
import SideMenu from './components/Sidemenu/SideMenu';
import style from './style.module.css'

function App() {
  return (
    <div>
      <Router>
        <Galnavbar></Galnavbar>
        <div className={style.body} style={{heigh:'100%'}}>
          <SideMenu></SideMenu>
          <Routes>
            <Route path="/" element={<FormPage/>}/>
            <Route path="/predict" element={<FormPage/>}/>
            <Route path="/addmodel" element={<AddModelPage/>}/>
            <Route path="/train" element={<TrainModelPage/>}/>
            <Route path="/info" element={<InfoPage/>}/>
          </Routes>
        </div>
      </Router>
    </div>

  );
}

export default App;
