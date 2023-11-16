import React, { useState } from 'react';
const InputImages = () => {
    const [image, setImage] = useState('');

    const handleImageChange = (e : any) => {
        setImage(URL.createObjectURL(e.target.files[0]));
    };
    const searchHandler = () => {
        console.log("njay")
    };
    return (
        <>
            <div className="flex w-ful justify-between p-10">
                <div className="flex justify-center items-center p-10">
                {
                    image ? (
                        <div className="max-w-sm mx-auto overflow-hidden bg-[#d9d9d9] rounded-lg shadow-md w-96">
                            <img className="object-cover w-full" src={image} alt="Your Image"></img>
                        </div>
                    ) : (
                        <div className="max-w-sm mx-auto overflow-hidden bg-[#d9d9d9] rounded-lg shadow-md w-96 h-64">
                            <img className="object-cover w-full" src={image}></img>
                        </div>
                    )
                }
                
                </div>
                <div className="flex justify-between items-center p-10 flex-col h-72">
                    <p>Image Input</p>
                    
                    <label className="bg-[#006cdb] py-2 rounded-lg w-48 text-white mt-2 cursor-pointer text-center">
                        <input id="image-input" className="hidden" type="file" accept='image/*' onChange={handleImageChange}/>
                        Input an image
                    </label>
                    <div className="h-16"></div>
                    <div className="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in">
                        <input type="checkbox" name="toggle" id="toggle" className="toggle-checkbox absolute block w-6 h-6 rounded-full bg-blue-500 border-4 appearance-none cursor-pointer"/>
                        <label htmlFor="toggle" className="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer"></label>
                    </div>
                    <button className="bg-[#006cdb] py-2 rounded-full text-white mt-2 w-48" onClick={searchHandler}>Search</button>
                </div>
            </div>
        </>
    )
}
export default InputImages