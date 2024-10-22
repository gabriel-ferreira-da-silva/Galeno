import React, { useEffect } from "react";
import { useState } from "react";
import DiseaseSelect from "../FormsPage/DiseaseSelect/DiseaseSelect";
import axios from "axios";
import style from "./style.module.css"
import { NormalButton } from "../commom/buttons/Buttons";
export default function ModelForm(){

    const [disease, setDiseases] = useState([]);
    const [file, setFile] = useState(null);

    function handleChange(event) {
        setFile(event.target.files[0])
      }
      
    function handleSubmit(event) {
        event.preventDefault()
        const url = 'http://localhost:3000/api/models/add';
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
            <h1> Fill the model form</h1>
            <div className={style.container}>
                
                <div className={style.inputHolder}>
                    <div>Name: </div>
                    <input></input>
                </div>
                <div className={style.inputHolder}>
                    <div>Type:</div>
                    <input type="textarea"></input>
                </div>
                <div className={style.inputHolder}>
                    <div>Disease: </div>
                    <DiseaseSelect
                        onDiseaseSelect={setDiseases}
                        text={""}
                    ></DiseaseSelect>
                </div>

                <div className={style.inputHolder}>
                    <div>Description: </div>
                    <input></input>
                </div>

                <div className={style.inputHolder}>
                    <div>Output Description: </div>
                    <input></input>
                </div>

                <div className={style.inputHolder}>
                    <div>Upload Model:</div>
                    <label for="file-upload" className={style.fileInput}>
                            Browse
                        </label>
                    <input id="file-upload" type="file"  onChange={handleChange}/>
                    {file?
                    <div>{file.name}</div>
                    :
                    <div>No file</div>
                    }
                </div>
                <div className={style.NormalButton} onClick={handleSubmit}>
                    submit
                </div>

            </div>
        </div>
        
    );
}