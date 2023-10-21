import logo from './logo.svg';
import './App.css';
import Upload from './components/Upload';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact Component={Upload} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
