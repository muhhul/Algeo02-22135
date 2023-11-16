import React, { useState } from 'react';
import ToggleSwitch from './components/ToggleSwitch';
const InputImages = () => {
    const [image, setImage] = useState('');
    
    const handleImageChange = (e : any) => {
        setImage(URL.createObjectURL(e.target.files[0]));
    };
    const isTexture = false;
    
    return (
        <>
            <form action="">
                <div className="flex w-ful justify-between p-10 w-full">
                    <div className="flex justify-center items-center p-10 w-full">
                    {
                        image ? (
                            <div className="overflow-hidden bg-black rounded-lg shadow-md w-full h-80">
                                <img className="object-contain w-full h-full" src={image} alt="Your Image"></img>
                            </div>
                        ) : (
                            <div className="overflow-hidden bg-[#d9d9d9] rounded-lg shadow-md w-full h-80"></div>
                        )
                    }
                    
                    </div>
                    <div className="flex justify-between items-center p-10 flex-col h-72">
                        <p className="text-blue-500 font-extrabold font-poppins">Image Input</p>
                        
                        <label className="bg-blue-500 hover:bg-blue-600 py-2 rounded-lg w-48 text-white mt-2 cursor-pointer text-center">
                            <input id="image-input" className="hidden" type="file" accept='image/*' onChange={handleImageChange}/>
                            Select Image
                        </label>
                        <div className="h-16"></div>
                        <div className="flex">
                            <span className="mr-3.5 font-poppins text-blue-500 font"> Color </span>
                            <ToggleSwitch isChecked={isTexture}/>
                            <span className="ml-1 font-poppins text-blue-500"> Texture </span>
                        </div>
                        <button type='submit' className="transition-all duration-500 bg-size-200 bg-pos-0 hover:bg-pos-100 font-poppins font-extrabold bg-gradient-to-r from-blue-600 to-purple-600 py-2 rounded-full text-white mt-2 w-48">Search</button>
                    </div>
                </div>
            </form>
        </>
    )
}

export default InputImages