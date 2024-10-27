import React from "react";
import { useState } from "react";
import InputSelect from "../../commom/inputSelect/InputSelect";
import { trainModel } from "../../../services/commomServices";
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
            <InputSelect
            options={colums}
            text={"select target atribute:"}
            handleChange={handleSelect}
            ></InputSelect>

            <button onClick={handleSubmit}>
                Submit
            </button>
        </div>
    )

}

export default SelectSubtmit;
