"use client"
import React, { useState } from 'react';
import Link from 'next/link';

const ImageGallery = ({ images } : any) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [imagesPerPage] = useState(8);

  // Get current images
  const indexOfLastImage = currentPage * imagesPerPage;
  const indexOfFirstImage = indexOfLastImage - imagesPerPage;
  const currentImages = images.slice(indexOfFirstImage, indexOfLastImage);

  // Change page
  const paginate = (pageNumber : any) => setCurrentPage(pageNumber);

  return (
    <div>
        <div className='flex justify-between p-5'>
            <p>Result</p>
            <p>54 Results in 0.57 seconds</p>
        </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {currentImages.map((image : any, index : any) => (
          <img key={index} src={image.src} alt={image.alt} className="object-cover h-48 w-full" />
        ))}
      </div>
      <Pagination
        imagesPerPage={imagesPerPage}
        totalImages={images.length}
        paginate={paginate}
      />
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
                <li className="mx-1 my-5 px-4 py-2 bg-blue-500 text-white rounded-lg cursor-pointer">
                    {number}
                </li>
            </div>
        ))}
      </ul>
    </nav>
  );
};

export default ImageGallery;
