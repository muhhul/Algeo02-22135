import React from "react"
import axios from "axios"

function App() {
  const [data,setData] = React.useState([]);
  const alamat_endpoint = "http://localhost:5000/api/data";
  React.useEffect(()=>{
    axios.get(alamat_endpoint).then(res => setData(res.data));
  },[]);

console.log(data);

  return (
    <div className="App">
      
    </div>
  );
}

export default App;
