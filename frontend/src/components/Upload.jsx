import React from 'react'
import { useState, useRef } from 'react';
const Upload = () => {

    const [file, setFile] = useState("");
    const [fileType, setFileType] = useState("")
    const inputRef = useRef(null);

    const handleUploadClick = () => {
        inputRef.current?.click();
    };

    const handleFileChange = (e) => {
        if (!e.target.files) {
            return;
        }
        setFile(e.target.files[0]);

        const splitString = e.target.files[0].name.split(".");
        setFileType(splitString.pop())
        console.log(e.target.files)
        console.log(fileType)
    };

    return (
        <div>
            {/* <button className="bg-purple-500 text-white">
      Click me!
    </button> */}
            <div>Upload a file:</div>

            <button onClick={handleUploadClick}>
                {file ? `${file.name}` : 'Click to select'}
            </button>
            <input
                type="file"
                ref={inputRef}
                onChange={handleFileChange}
                style={{ display: 'none' }}
            />
        </div>
    )
}

export default Upload