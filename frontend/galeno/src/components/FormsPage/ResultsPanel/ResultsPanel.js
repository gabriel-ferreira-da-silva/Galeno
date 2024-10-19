import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { modelPredict } from '../../../services/commomServices';

function ResultsPanel({model, input}){
    const [results, setResults] = useState(null);
    let description = "";
    let res = "";
    useEffect(()=>{
        const predict = async (modelName,inputArray)=>{
            try{
                if((modelName && inputArray)==false) return;
                const response = await modelPredict(modelName,inputArray);
                setResults(response);
            }catch(e){
                setResults(null);
            }
            
        }
        
        predict(model,input)  
    },[model, input])
    
    
    return (
        <div>
            {
                results ?
                <div>
                    <p>results</p>
                    <p>{"results: " +res}</p>
                    <p>{description}</p>
                </div>
                 :
                <div></div>

            }
        </div>
    );    
  
};

export default ResultsPanel;