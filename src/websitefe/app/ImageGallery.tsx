"use client"
import React, { useState } from 'react';
import Link from 'next/link';
import { time } from 'console';

const ImageGallery = ({ resultData,resultTime } : any) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [imagesPerPage] = useState(6);
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageClick = async (image:any) => {
    try {
      const module = await import(`../../backend/upload_images/${image.nama_file}`);
      setSelectedImage(module.default);
    } catch (error) {
      console.error('Error loading image:', error);
    }
  };
  const handleFileChange = async(e:any) => {
    console.log("masuk satu");
    const folder = e.target.files[0];
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:8000/hapusdataset/', {
        method: 'POST',
        body: "tes",
      });

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }

    for (let i = 0; i < e.target.files.length; i++) {
      const file = e.target.files[i];
      const formData = new FormData();
      formData.append('file', file);
      console.log("masuk 2");
      try {
        const response = await fetch('http://127.0.0.1:8000/upload/', {
          method: 'POST',
          body: formData,
        });
  
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }
    
    try {
      const response = await fetch('http://127.0.0.1:8000/uploadtodatabase/', {
        method: 'POST',
        body: "tes",
      });

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  

  // Get current images
  const indexOfLastImage = currentPage * imagesPerPage;
  const indexOfFirstImage = indexOfLastImage - imagesPerPage;
  const currentData = resultData.slice(indexOfFirstImage, indexOfLastImage);

  // Change page
  const paginate = (pageNumber : any) => setCurrentPage(pageNumber);

  return (
    <div>
        <div className='flex justify-between my-5'>
            <p className="text-blue-500 font-extrabold font-poppins">Result</p>
            <p className="font-poppins">{resultData.length} results in {resultTime.toFixed(2)} seconds</p>
        </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-4">
        {currentData.map((data : any, index : any) => (
        <figure key={index} className="w-full relative rounded-md drop-shadow-lg flex justify-center">
          <img src={`data:image/jpeg;base64,${data.images}`} alt={"image"} className="object-cover h-48 w-full" />
          <figcaption className="absolute bottom-0 z-90 w-3/4  px-5 py-2 text-white text-center text-sh ">
            <span className="text-l font-extrabold" style={{ textShadow: '0 0 5px black' }}>{data.persentase.toFixed(2)}%</span>
          </figcaption>
        </figure>
        ))}
      </div>
      <Pagination
        imagesPerPage={imagesPerPage}
        totalImages={resultData.length}
        paginate={paginate}
      />
      <hr className="w-full h-1 bg-[#d9d9d9]"></hr>
      <form action="">
        <div className="flex justify-center mb-10">
            <label className="transition-all duration-500 bg-size-200 bg-pos-0 hover:bg-pos-100 font-extrabold font-poppins bg-gradient-to-r from-blue-600 to-purple-600 py-2 rounded-lg w-48 text-white mt-2 cursor-pointer text-center">
                <input id="image-input" className="hidden" type="file" onChange={handleFileChange} directory="" webkitdirectory="" mozdirectory=""/>
                Upload Folder
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
