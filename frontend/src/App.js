import logo from './logo.svg';
import './App.css';
import Upload from './components/Upload';
import ToC from './components/ToC';
import flashcards from './components/flashcards';
import { BrowserRouter, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact Component={Upload} />
        <Route path="/toc" exact Component={ToC} />
        <Route path="/flashcards" exact Component={flashcards} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
