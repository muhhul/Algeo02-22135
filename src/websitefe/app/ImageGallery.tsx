"use client"
import React, { useState } from 'react';
import Link from 'next/link';

const ImageGallery = ({ images } : any) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [imagesPerPage] = useState(6);

  const [image, setImage] = useState('');

  const handleImageChange = (e : any) => {
      setImage(URL.createObjectURL(e.target.files[0]));
  };


  // Get current images
  const indexOfLastImage = currentPage * imagesPerPage;
  const indexOfFirstImage = indexOfLastImage - imagesPerPage;
  const currentImages = images.slice(indexOfFirstImage, indexOfLastImage);

  // Change page
  const paginate = (pageNumber : any) => setCurrentPage(pageNumber);

  return (
    <div>
        <div className='flex justify-between my-5'>
            <p className="text-blue-500 font-extrabold font-poppins">Result</p>
            <p className="font-poppins">54 Results in 0.57 seconds</p>
        </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-4">
        {currentImages.map((image : any, index : any) => (
        <figure key={index} className="w-full relative rounded-md drop-shadow-lg flex justify-center">
          <img  src={image.src} alt={image.alt} className="object-cover h-48 w-full" />
          <figcaption className="absolute bottom-0 z-90 w-3/4  px-5 py-2 text-white text-center">
            <span className="text-l font-bold">{image.percentage}%</span>
          </figcaption>
        </figure>
        ))}
      </div>
      <Pagination
        imagesPerPage={imagesPerPage}
        totalImages={images.length}
        paginate={paginate}
      />
      <hr className="w-full h-1 bg-[#d9d9d9]"></hr>
      <form action="">
        <div className="flex justify-center mb-10">
            <label className="transition-all duration-500 bg-size-200 bg-pos-0 hover:bg-pos-100 font-extrabold font-poppins bg-gradient-to-r from-blue-600 to-purple-600 py-2 rounded-lg w-48 text-white mt-2 cursor-pointer text-center">
                <input id="image-input" className="hidden" type="file" onChange={handleImageChange} directory="" webkitdirectory="" mozdirectory=""/>
                Upload Dataset
            </label>
        </div>
      </form>
    </div>
  );
};

const Pagination = ({ imagesPerPage, totalImages, paginate } : any) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(totalImages / imagesPerPage); i++) {
    pageNumbers.push(i);
  }

  return (
    <nav className="flex justify-center mt-4">
      <ul className="flex">
        {pageNumbers.map(number => (
            <div key={number} onClick={() => paginate(number)} className="text-decoration-none">
                <li className="mx-1 my-5 px-4 py-2 border-solid border-blue-600 border-2 bg-white hover:bg-blue-600 text-blue-600 hover:text-white rounded-lg cursor-pointer">
                    {number}
                </li>
            </div>
        ))}
      </ul>
    </nav>
  );
};

export default ImageGallery;
