import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchAvailableDiseases } from '../../../services/commomServices';
import InputSelect from '../../commom/inputSelect/InputSelect';
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
            <InputSelect
                handleChange={handleDiseaseChange}
                options={diseases}
            ></InputSelect>
        </div>
    );    
  
};

export default DiseaseSelect;