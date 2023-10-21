import React, { useState, useEffect } from 'react';

const Summary = () => {
    const [summary, setSummary] = useState('');

    useEffect(() => {
        fetch('/api/summary')
            .then((response) => response.json())
            .then((data) => {
                setSummary(data.summary);
            });
    }, []);

    return (
        <div>
            {summary && <p>{summary}</p>}
            {!summary && <p>Loading summary...</p>}
        </div>
    );
};

export default Summary;