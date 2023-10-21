const Chapters = () => {
    return (
        <ul>
            {chapters.map((chapter) => (
                <li key={chapter.title}>{chapter.title}</li>
            ))}
        </ul>
    );
};


const App = () => {
    const [currentChapter, setCurrentChapter] = useState(0);

    const handleChapterClick = (chapter) => {
        setCurrentChapter(chapter);
    };

    return (
        <div>
            <ul>
                {chapters.map((chapter) => (
                    <li key={chapter.title}>
                        <button onClick={() => handleChapterClick(chapter)}>{chapter.title}</button>
                    </li>
                ))}
            </ul>
            <div>{chapters[currentChapter].content}</div>
        </div>
    );
};
