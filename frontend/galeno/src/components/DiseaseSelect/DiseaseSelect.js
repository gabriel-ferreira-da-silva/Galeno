import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchAvailableDiseases } from '../../services/commomServices';

function DiseaseSelect({onDiseaseSelect}){
    const [diseases, setDiseases] = useState([]);

    useEffect(()=>{
        const loadAvailableDiseases = async () =>{
            const response = await fetchAvailableDiseases();
            setDiseases(response);
        }
        loadAvailableDiseases();
    },[])

    const handleDiseaseChange = (event) => {
        console.log(event.target.value);
        onDiseaseSelect(event.target.value);
      };

    return (
        <div>
            <label>Select the disease you want diagnosis for: </label>
             <select onChange={handleDiseaseChange}>
                <option value={""} selected>---------</option>
                {   
                    diseases.map((disease, index)=>(
                        <option key={index} value={disease}> {disease}</option>
                    ))
                }
            </select>
            
        </div>
    );    
  
};

export default DiseaseSelect;