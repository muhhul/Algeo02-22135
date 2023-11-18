'use client'
import {useState} from 'react'
import InputImage from "./InputImage"
import ImageGallery from "./ImageGallery"
const ClientPage = () => {
    const [result,setResult] = useState([])
    const [time,setTime] = useState(0)
    const handleUpload = async ({isChecked,image}:{isChecked:any,image:any}) => {
        console.log(isChecked,image)

        const formData = new FormData();
        formData.append("file", image);
        // try {
        //   const response = await axios.post("http://127.0.0.1:8000/uploadfile/", formData, {
        //     headers: {
        //       "Content-Type": "multipart/form-data",
        //     },
        //   });
        try {
            if(isChecked){
                const endPoint = "http://127.0.0.1:8000/uploadfile/";
                const res = await fetch(endPoint, {
                  method: "POST",
                  body: formData,
                })
                const data = await res.json();
                console.log(data)
                setResult(data)
            }else{
                const endPoint = "http://127.0.0.1:8000/uploadfile2/";
                const res = await fetch(endPoint, {
                  method: "POST",
                  body: formData,
                })
                const data = await res.json();
                setResult(data)
            }
        }
        catch (err) {
        }
        try {
            const response = await fetch('http://127.0.0.1:8000/time/', {
              method: 'POST',
              body: "tes",
            });
            const data = await response.json();
            setTime(data);
          } catch (error) {
          }
      
    };
    return <div>
        <InputImage onSearch={handleUpload} />
        <hr className="w-full h-1 bg-[#d9d9d9]"></hr>
        <ImageGallery resultData={result} resultTime={time}/>
    </div>
}

export default ClientPage