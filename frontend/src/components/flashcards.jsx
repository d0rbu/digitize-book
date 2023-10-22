import React, { useState } from 'react'
import './flash.css'; // Import your CSS file;

function Flashcards() {
  const [flashcards, setFlashcards] = useState(SAMPLE_FLASHCARDS);
  return (
    <div className="card-grid">
      {flashcards.map((flashcard) => (
        <Flashcard flashcard={flashcard} key={flashcard.id} />
      ))}
    </div>
  );
}

const SAMPLE_FLASHCARDS = [
  {
    id: 1,
    question: 'What is 2 + 2?',
    answer: '4',
  },
  {
    id: 2,
    question: 'What is 3 + 3?',
    answer: '6',
  },
];

const Flashcard = ({ flashcard }) => {
  const [isFlipped, setIsFlipped] = useState(false);

  const flipCard = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div className={`card ${isFlipped ? 'flipped' : ''}`} onClick={flipCard}>
      <div className="card-inner">
        <div className="card-front">
          <p>{flashcard.question}</p>
        </div>
        <div className="card-back">
          <p>{flashcard.answer}</p>
        </div>
      </div>
    </div>
  );
};

export default Flashcards;

// import React, { useState, useEffect } from 'react';
// import './flash.css'; // Import your CSS file;

// function Flashcards() {
//   const [flashcards, setFlashcards] = useState([]);

//   useEffect(() => {
//     // Fetch flashcard data from your backend API
//     fetch('your-backend-api-url')
//       .then((response) => response.json())
//       .then((data) => setFlashcards(data))
//       .catch((error) => console.error('Error fetching data', error));
//   }, []);

//   return (
//     <div className="card-grid">
//       {flashcards.map((flashcard) => (
//         <Flashcard flashcard={flashcard} key={flashcard.id} />
//       ))}
//     </div>
//   );
// }

// const Flashcard = ({ flashcard }) => {
//   const [isFlipped, setIsFlipped] = useState(false);

//   const flipCard = () => {
//     setIsFlipped(!isFlipped);
//   };

//   return (
//     <div className={`card ${isFlipped ? 'flipped' : ''}`} onClick={flipCard}>
//       <div className="card-inner">
//         <div className="card-front">
//           <p>{flashcard.question}</p>
//         </div>
//         <div className="card-back">
//           <p>{flashcard.answer}</p>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default Flashcards;

