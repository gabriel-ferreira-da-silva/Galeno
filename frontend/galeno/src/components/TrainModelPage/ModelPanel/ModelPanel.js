import React, { useEffect, useState } from "react";
import { fetchModelByName } from "../../../services/commomServices";
import style from "./style.module.css"
function ModelPanel({modelname,datafile}){

    const [model, setModel] = useState(null)
    const [file, setFile] = useState(null)
    useEffect(()=>{
        const fetchModel = async(name)=>{
            try{
                const response = await fetchModelByName(name);
                setModel(response)
            }catch(error){
                throw error
            }
        }
        if(modelname){
            fetchModel(modelname)
        }
        console.log(model)
        console.log("======================")
    },[modelname])
    
    const handleChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
    };


    return(
        <div>
            {model?
                <div>
                    <div>
                        {"name: "}
                        {model.name}
                    </div>
                    <div>
                        {"type: "}
                        <div>{model.type}</div>
                    </div>
                    <div>
                        {"disease: "}
                        <div>{model.disease}</div>
                    </div>
                    <div>
                        {"description: "}
                        <div>{model.description}</div>
                    </div>
                    <div className={style.inputModelHolder}>
                        <div></div>
                        <label htmlFor="file-upload" className={style.fileInput}>
                            <div>Upload Model</div>
                        </label>
                        <input id="file-upload" type="file" onChange={handleChange} />
                        
                        {file ? <div className={style.filetitle}>
                                    <p>model: {file.name}</p>
                                </div> 
                                : 
                                <div></div>}

                    </div>
                    <button className={style.NormalButton} onClick={handleSubmit}>
                        Submit
                    </button>
                </div>

            :
                <div></div>
            }
        </div>
    )
}

export default ModelPanel