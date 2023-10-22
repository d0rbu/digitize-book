import React, { useState, useEffect } from 'react';
import './TOC.css'; // Import your CSS file

// const TableOfContents = () => {
//     const [chapters, setChapters] = useState([]);

//     useEffect(() => {
//       // Fetch chapters from your backend API
//       fetch('your-backend-api-url')
//         .then((response) => response.json())
//         .then((data) => setChapters(data))
//         .catch((error) => console.error('Error fetching data', error));
//     }, []);

const TableOfContents = () => {
    // Sample table of contents data
    const tableOfContents = [
        { title: 'Chapter 1: Introduction', id: 'chapter1' },
        { title: 'Chapter 2: Main Content', id: 'chapter2' },
        { title: 'Chapter 3: Conclusion', id: 'chapter3' },
    ];

    return (
        <div className="table-of-contents">
            <h2>Table of Contents</h2>
            <ul>
                {tableOfContents.map((chapter) => (
                    <li key={chapter.id}>
                        <a href={`#${chapter.id}`}>{chapter.title}</a>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TableOfContents;