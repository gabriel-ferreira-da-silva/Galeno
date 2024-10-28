import React from "react";
import { useState } from "react";
import InputSelect from "../../commom/inputSelect/InputSelect";
import { trainModel } from "../../../services/commomServices";
import style from "./style.module.css"
import Fade from "react-reveal/Fade"

function SelectSubtmit({colums,columTarget, setColumtarget,model,file}){

    const handleSelect = async (event)=>{
        event.preventDefault();
        console.log(event.target.value);
        setColumtarget(event.target.value);
    }
    
    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!file || !model || !columTarget) {
            console.error("Please select all required inputs before submitting.");
            console.log(file)
            console.log(model)
            console.log(columTarget)
            return;
        }

        const formData = new FormData();
        formData.append("traindata", file);
        formData.append("model", model);
        formData.append("target", columTarget);

        try {
            const response = await trainModel(formData);
            console.log("Response:", response);
        } catch (error) {
            console.error("Error during model training:", error);
        }
    };

    return(
        <div>
            {
                model && file && colums && 
                <Fade>
                    <div className={style.container}>
                        <InputSelect
                        options={colums}
                        text={"select target atribute:"}
                        handleChange={handleSelect}
                        ></InputSelect>
            
                        <button className={style.NormalButton} onClick={handleSubmit}>
                            Submit
                        </button>
                    </div>
                </Fade>
            }
            
        </div>
    )

}

export default SelectSubtmit;
