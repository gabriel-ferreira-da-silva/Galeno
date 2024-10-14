import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchModelsInputDescriptionByName } from '../../services/commomServices';

function ModelForm({model}){
    const [inputs, setInputs] = useState([]);
    useEffect(()=>{
        const fetchInputDescription = async(modelname)=>{
            if(modelname=="") return;
            const response = await fetchModelsInputDescriptionByName(modelname)
            setInputs(response);
            console.log(inputs)
        }

        fetchInputDescription(model)

    },[model])
    return (
        <div>
            {
                model?
                <div>
                    <label> fill the form</label>
                    {
                        inputs.map((input, index)=>(
                            <div key={index}>
                                <label>{input}</label> 
                                <input></input>
                                <br></br>
                            </div>
                        ))
                    }
                </div>
                :
                <div></div>
             
            }

        </div>
    );    
  
};

export default ModelForm;