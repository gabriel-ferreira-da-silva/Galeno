import React, { useEffect } from "react";
import { useState } from "react";
import { fetchAvailableModels } from "../../../services/commomServices";
import InputSelect from "../../commom/inputSelect/InputSelect";
export default function ModelsSelect({onModelSelect}){

    const [models, setModels] = useState([]);
    
    useEffect(()=>{
        const fetchModels = async ()=> {
            try{
                const response = await fetchAvailableModels(); 
                setModels(response)
            }catch(error){
                console.error("error fetching models")
            }
        }
        fetchModels();
        console.log(models)
    },[])


    const handleModelChange = (event)=>{
        onModelSelect(event.target.value);
    }
    return(
        <div>
            <InputSelect
                handleChange={handleModelChange}
                options={models}
                text={"select model to train"}
            ></InputSelect>
        </div>
    );
}