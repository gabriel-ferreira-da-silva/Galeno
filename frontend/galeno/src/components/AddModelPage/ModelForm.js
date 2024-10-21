import React, { useEffect } from "react";
import { useState } from "react";
import DiseaseSelect from "../FormsPage/DiseaseSelect/DiseaseSelect";
import axios from "axios";
export default function ModelForm(){

    const [disease, setDiseases] = useState([]);
    const [file, setFile] = useState(null);

    function handleChange(event) {
        setFile(event.target.files[0])
      }
      
    function handleSubmit(event) {
        event.preventDefault()
        const url = 'http://localhost:3000/uploadFile';
        const formData = new FormData();
        formData.append('file', file);
        formData.append('fileName', file.name);
        const config = {
          headers: {
            'content-type': 'multipart/form-data',
          },
        };
        axios.post(url, formData, config).then((response) => {
          console.log(response.data);
        });
      }

    return (
        <div>
            <div>
                <div>
                    <p>name</p>
                    <input></input>
                </div>
                <div>
                    <p>type</p>
                    <input type="textarea"></input>
                </div>
                <div>
                    <p>disease</p>
                    <DiseaseSelect
                        onDiseaseSelect={setDiseases}
                        text={""}
                    ></DiseaseSelect>
                </div>

                <div>
                    <p>description</p>
                    <input></input>
                </div>

                <div>
                    <p>output description</p>
                    <input></input>
                </div>

                <div>
                    <p>upload model</p>
                    <form onSubmit={handleSubmit}>
                        <h1>React File Upload</h1>
                        <input type="file" onChange={handleChange}/>
                        <button type="submit">Upload</button>
                    </form>
                </div>
                
            </div>
        </div>
        
    );
}