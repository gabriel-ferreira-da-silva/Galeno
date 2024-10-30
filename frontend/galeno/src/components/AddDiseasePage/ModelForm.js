import React, { useState } from "react";
import style from "./style.module.css";
import { addNewDisease } from "../../services/commomServices";
import Fade from "react-reveal/Fade";
import InputDescriptionHolder from "./InputDescriptionHolder/InputDescriptionHolder";

export default function ModelForm() {
    const [disease, setDisease] = useState("");
    const [inputDesc, setInputDesc] = useState([]);
    const [file, setFile] = useState(null);
    const [data, setData] = useState({
        name: "",
        description: "",
        input_description: [],
        scaler: null
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
        formData.append("description", data.description);
        formData.append("disease", disease);
        formData.append("input_description", JSON.stringify(inputDesc));  // Convert array to JSON string
        formData.append("scaler", file);

        try {
            const response = await addNewDisease(formData);
            console.log("Model added:", response);
        } catch (error) {
            console.error("Error adding model:", error);
        }
    };

    const [inputHolders, setInputHolders] = useState([
        { id: 1, name: "name", mainValue: "", descriptionValue: "" }
    ]);

    const handleAddInput = () => {
        setInputHolders([
            ...inputHolders,
            {
                id: inputHolders.length + 1,
                name: `name${inputHolders.length + 1}`,
                mainValue: "",
                descriptionValue: ""
            }
        ]);
    };

    const handleMainChange = (id, newValue) => {
        setInputHolders(inputHolders.map(holder =>
            holder.id === id ? { ...holder, mainValue: newValue } : holder
        ));
    };

    const handleDescriptionChange = (id, newValue) => {
        setInputHolders(inputHolders.map(holder =>
            holder.id === id ? { ...holder, descriptionValue: newValue } : holder
        ));
    };

    const handleInputDescSubmit = () => {
        const values = inputHolders.map(holder => ({
            input: holder.mainValue,
            description: holder.descriptionValue
        }));
        setInputDesc(values);  // Update `inputDesc` state with new values
    };

    return (
        <div>
            <Fade bottom duration={1000}>
                <h1>Fill the Disease form</h1>
                <div className={style.container}>
                    <div className={style.inputHolder}>
                        <div>Name: </div>
                        <input name="name" onChange={handleInputChange} />
                    </div>

                    <div className={style.inputHolder}>
                        <div>Disease:</div>
                        <input name="disease" onChange={(e) => setDisease(e.target.value)} />  {/* Fixed handler */}
                    </div>

                    <div className={style.textHolder}>
                        <div>Description: </div>
                        <textarea className={style.description} name="description" onChange={handleInputChange} />
                    </div>

                    <div className={style.inputDescriptionHolder}>
                        {inputHolders.map(holder => (
                            <InputDescriptionHolder
                                key={holder.id}
                                name={holder.name}
                                mainValue={holder.mainValue}
                                descriptionValue={holder.descriptionValue}
                                onMainChange={(e) => handleMainChange(holder.id, e.target.value)}
                                onDescriptionChange={(e) => handleDescriptionChange(holder.id, e.target.value)}
                            />
                        ))}

                        <button className={style.NormalButton} onClick={handleAddInput}>Add new input</button>
                        <button className={style.NormalButton} onClick={handleInputDescSubmit}>Confirm inputs</button>
                    </div>
                    
                    <div className={style.inputModelHolder}>
                        <label htmlFor="file-upload" className={style.fileInput}>
                            <div>Upload Scaler</div>
                        </label>
                        <input id="file-upload" type="file" onChange={handleChange} />
                        
                        {file ? <div className={style.filetitle}>
                                    <p>Model: {file.name}</p>
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
