import React, { useState, useEffect } from 'react';

const Quiz = () => {
    const [questions, setQuestions] = useState([]);
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [score, setScore] = useState(0);

    useEffect(() => {
        fetch('/api/questions')
            .then((response) => response.json())
            .then((data) => {
                setQuestions(data);
            });
    }, []);

    const handleAnswerClick = (answer) => {
        if (answer === questions[currentQuestion].correct_answer) {
            setScore(score + 1);
        }

        if (currentQuestion < questions.length - 1) {
            setCurrentQuestion(currentQuestion + 1);
        } else {
            // Quiz is finished
        }
    };

    return (
        <div>
            {questions.length > 0 && (
                <div>
                    <h2>Question {currentQuestion + 1} of {questions.length}</h2>
                    <p>{questions[currentQuestion].question}</p>
                    <ul>
                        {questions[currentQuestion].answers.map((answer) => (
                            <li key={answer}>
                                <button onClick={() => handleAnswerClick(answer)}>{answer}</button>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
            {questions.length === 0 && <p>Loading questions...</p>}
        </div>
    );
};

export default Quiz;
