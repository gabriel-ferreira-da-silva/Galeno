import React, { useState } from "react";
import DiseaseSelect from "../FormsPage/DiseaseSelect/DiseaseSelect";
import style from "./style.module.css";
import { addNewModel } from "../../services/commomServices";

import Fade from "react-reveal/Fade"


export default function ModelForm() {
    const [disease, setDiseases] = useState("");
    const [file, setFile] = useState(null);
    const [data, setData] = useState({
        name: "",
        type: "",
        description: "",
        disease: "",
        output_description: "",
        model: null
    });

    const handleChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setData((prevData) => ({
            ...prevData,
            [name]: value
        }));
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();

        formData.append("name", data.name);
        formData.append("type", data.type);
        formData.append("description", data.description);
        formData.append("disease", disease); // use the state from DiseaseSelect
        formData.append("output_description", data.output_description);
        formData.append("model", file);

        try {
            const response = await addNewModel(formData);
            console.log("Model added:", response);
        } catch (error) {
            console.error("Error adding model:", error);
        }
    };

    return (
        <div>
            <Fade bottom duration={1000}>
                <h1> Fill the model form</h1>
                <div className={style.container}>
                    <div className={style.inputHolder}>
                        <div>Name: </div>
                        <input name="name" onChange={handleInputChange} />
                    </div>
                    <div className={style.inputHolder}>
                        <div>Type:</div>
                        <input name="type" onChange={handleInputChange} />
                    </div>
                    <div className={style.inputHolder}>
                        <div>Disease: </div>
                        <DiseaseSelect
                            onDiseaseSelect={(selectedDisease) => setDiseases(selectedDisease)}
                        />
                    </div>
                    <div className={style.textHolder}>
                        <div>Description: </div>
                        <textarea className={style.description} name="description" onChange={handleInputChange} />
                    </div>
                    <div className={style.textHolder}>
                        <div>Output Description: </div>
                        <textarea className={style.description} onChange={handleInputChange} />
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
            </Fade>
        </div>
    );
}
