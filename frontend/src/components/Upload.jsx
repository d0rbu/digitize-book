import React from 'react'
import "./Upload.css";
import { useState, useRef } from 'react';
import { Button } from "@material-tailwind/react";
import frontImage from '../images/front.png';
import logo from '../images/logo.png';
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

    // let buttonCode = <div style={{ background: 'radial-gradient(circle at 10% 20%, rgb(6, 123, 239) 14.2%, rgb(180, 180, 255) 89.5%)' }}
    //     className='border-slate-500 border-[1.3px] 
    //     font-semibold text-xs text-white
    //      rounded-3xl py-4 px-20 
    //      text-center ml-0 mt-[50%] '>
    //     <div className='uploadText'>Upload a file: </div>

    //     <button onClick={handleUploadClick} className='uploadText mt-[4px]'>
    //         {file ? (file.name.length <= 7 ? file.name : `${file.name.slice(0, 8)}...`) : 'Click to select'}

    //     </button>
    //     <input
    //         type="file"
    //         ref={inputRef}
    //         onChange={handleFileChange}
    //         style={{ display: 'none' }}
    //     />
    // </div>
    const mtClass = file.length === 0 ? 'mt-[50%]' : '';

    let buttonCode = (
      <div
        style={{
          background: 'radial-gradient(circle at 10% 20%, rgb(6, 123, 239) 14.2%, rgb(180, 180, 255) 89.5%)'
        }}
        className={`border-slate-500 border-[1.3px] 
            font-semibold text-xs text-white
             rounded-3xl py-4 px-20 
             text-center ml-0 ${mtClass}`}
      >
        <div className='uploadText'>Upload a file: </div>
    
        <button onClick={handleUploadClick} className='uploadText mt-[4px]'>
        {file ? (file.name.length <= 7 ? file.name : `${file.name.slice(0, 8)}...`) : 'Click to select'}
        </button>
    
        <input
          type="file"
          ref={inputRef}
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />
      </div>
    );
    return (
        <div>

            <div className=" flex flex-row w-screen">
                <div className="basis-3/5 col-span-3  h-full bg-white z-10">
                    <div className="flex flex-col justify-center  items-center mr-[35%]">
                        <div className="titleF flex font-bold absolute text-[60px] mt-[100px]">
                            <p className={file ? '' : 'mt-[70%]'}>sardineNotes</p>
                        </div>
                        {!file ? <div className='landingMessage tracking-wide mt-[500px]  absolute  '>
                            <p class="mt-[50%]">digitize your studying using AI. study harder, study better, study smarter. </p>
                        </div> : <></>}


                    </div>

                    <div className={` ${!file ? 'flex items-center  mr-[35%]  justify-center h-screen' : ''} `}>
                        {!file ? buttonCode : <></>}
                    </div>
                    <div className="float-right -mt-[80%] -mr-[45%]">
                        <img src={frontImage} className=" " alt="Image Description" />
                    </div>
                </div>


                <div className="basis-2/5 col-span-2  h-screen  " style={{ background: 'linear-gradient(106.5deg, rgba(255, 215, 185, 0.91) 23%, rgba(223, 159, 247, 0.8) 93%)' }}>
                    <div className={`${file ? 'flex flex-row justify-end mt-5 mr-5 ml-auto' : ''} `}>

                        {file ? buttonCode : <></>}
                    </div>

                </div>
            </div>
        </div>
    )
}

export default Upload