"use client"
import React, { useState } from 'react';
import ImageGallery from './ImageGallery'
import InputImages from './InputImage'

export default function Home() {
  const [images, setImages] = useState([]);
  return (
    <>
      <div className="px-64">
        <div className="flex justify-center">
          <h1 className='font-poppins mt-10 text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600'>Reverse Image Search</h1>
        </div>
        <InputImages setImages={setImages} />
        <hr className="w-full h-1 bg-[#d9d9d9]"></hr>
        <ImageGallery images={images}/>
      </div>
    </>
  )
}
