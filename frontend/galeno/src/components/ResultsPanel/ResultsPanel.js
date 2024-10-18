import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { modelPredict } from '../../services/commomServices';

function ResultsPanel({model, input}){
    const [results, setResults] = useState(null);
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
                <label>Prediction: {JSON.stringify(results)}</label>
                :
                <div></div>

            }
        </div>
    );    
  
};

export default ResultsPanel;