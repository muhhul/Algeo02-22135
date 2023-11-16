"use client"
import ImageGallery from './ImageGallery'
import InputImages from './InputImage'

export default function Home() {
  const images = [
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 95},
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 90},
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 87},
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 87},
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 87},
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 85},
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 85 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2',percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1682687221038-404cb8830901?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8', alt: 'Image 1', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://images.unsplash.com/photo-1699727152109-b5b9592641ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
    { src: 'https://plus.unsplash.com/premium_photo-1699382168474-84c1ce570430?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8', alt: 'Image 2', percentage: 84.2 },
  ];
  return (
    <>
      <div className="px-64">
        <div className="flex justify-center">
          <h1 className='font-poppins mt-10 text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600'>Reverse Image Search</h1>
        </div>
        <InputImages />
        <hr className="w-full h-1 bg-[#d9d9d9]"></hr>
        <ImageGallery images={images}/>
      </div>
    </>
  )
}
