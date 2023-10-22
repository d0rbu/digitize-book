const App = () => {
    const [isValidFileUploaded, setIsValidFileUploaded] = useState(false);

    const handleFileUploaded = (isValid) => {
        if (isValid) {
            history.push('/components');
        }
    };

    return (
        <div>
            <Router>
                <Route path="/" exact>
                    <p>Please upload a valid file.</p>
                </Route>
                <Route path="/components">
                    <Chapters />
                    <Summary />
                    <Quiz />
                </Route>
            </Router>
        </div>
    );
}

