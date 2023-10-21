import React, { useState } from 'react';

const Flashcard = () => {
  const [flipped, setFlipped] = useState(false);

  const handleClick = () => {
    setFlipped(!flipped);
  };

  return (
    <div className="flashcard">
      {!flipped && (
        <div className="front" onClick={handleClick}>
          {question}
        </div>
      )}
      {flipped && (
        <div className="back" onClick={handleClick}>
          {answer}
        </div>
      )}
    </div>
  );
};

export default Flashcard;
