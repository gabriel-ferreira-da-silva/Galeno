import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchModelsNamesByDisease } from '../../services/commomServices';

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
                <div>
                <label>Select the model you want to use </label>
                <select onChange={handleModelChange}>
                    <option value={""} selected >---------</option>
                    {   
                        
                        models.map((model, index)=>(
                            <option key={index} value={model}> {model}</option>
                        ))
                    }
                </select>
                </div>
            
            : <div></div>}
        </div>
    );    
  
};

export default ModelSelect;