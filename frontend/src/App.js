import logo from './logo.svg';
import './App.css';
import Upload from './components/Upload';
import Flashcards from './components/flashcards';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Quiz from './components/Quiz';
import TableOfContents from './components/TableOfContents';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact Component={Upload} />
        <Route path="/flashcards" exact Component={Flashcards} />
        <Route path="/quiz" exact Component={Quiz} />
        <Route path="/TableOfContents" exact Component={TableOfContents} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
