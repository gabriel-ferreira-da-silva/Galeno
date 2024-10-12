import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchAvailableDiseases } from '../../services/commomServices';

function DiseaseSelect(){
    const [diseases, setDiseases] = useState([]);

    useEffect(()=>{
        const loadAvailableDiseases = async () =>{
            const response = await fetchAvailableDiseases();
            setDiseases(response);
        }

        loadAvailableDiseases();
    },[])

    return (
        <div>
            <label>Select the disease you want diagnosis for: </label>
             <select>
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