import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchModelsInputDescriptionByName } from '../../services/commomServices';

function ModelForm({model,disease,setForm}){
    const [inputs, setInputs] = useState([]);
    const [array, setArray] = useState([])
    useEffect(()=>{
        const fetchInputDescription = async(diseasename)=>{
            if(diseasename=="") return;
            const response = await fetchModelsInputDescriptionByName(diseasename)
            setInputs(response);
            setArray(new Array(response.length).fill(0));
        }

        fetchInputDescription(disease)

    },[disease])

    const updateArray = (event) => {
        const index = Number(event.target.name); 
        const value = Number(event.target.value);

        setArray((prevArray) => {
            const newArray = [...prevArray];
            newArray[index] = value; 
            return newArray; 
        });
    };

    const submitArray = ()=>{
        setForm(array);
    }

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
                                <input name={index} onChange={updateArray}></input>
                                <br></br>
                            </div>
                        ))
                    }
                    <button onClick={submitArray}>submit</button>
                </div>
                :
                <div></div>
            }

            

        </div>
    );    
  
};

export default ModelForm;