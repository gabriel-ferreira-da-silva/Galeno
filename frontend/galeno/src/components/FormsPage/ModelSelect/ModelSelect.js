import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchModelsNamesByDisease } from '../../../services/commomServices';
import InputSelect from '../../commom/inputSelect/InputSelect';
import Fade from "react-reveal/Fade"
function ModelSelect({onModelSelect,disease}){
    const [models, setModel] = useState([]);

    useEffect(()=>{
        const loadModelsNamesByDisease = async (diseaseName) =>{
            if(diseaseName=="") return;
            const response = await fetchModelsNamesByDisease(diseaseName);
            console.log("loaded models on");
            console.log(diseaseName);
            setModel(response);
        }
        loadModelsNamesByDisease(disease);
    },[disease])

    const handleModelChange = (event) => {
        onModelSelect(event.target.value);
      };

    return (
        <div>
            {disease!==""?
                <Fade bottom duration={1000}>
                    <InputSelect
                        handleChange={handleModelChange}
                        options={models}
                    ></InputSelect>
                </Fade>
            : <div></div>}
            
            
        </div>
    );    
  
};

export default ModelSelect;