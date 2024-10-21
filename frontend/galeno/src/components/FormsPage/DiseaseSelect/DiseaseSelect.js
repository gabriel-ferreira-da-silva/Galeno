import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import InputSelect from '../../commom/inputSelect/InputSelect';
import { loadAvailableDiseases } from './DiseaseSelect.utils';
function DiseaseSelect({onDiseaseSelect, text}){
    const [diseases, setDiseases] = useState([]);

    useEffect(()=>{

        loadAvailableDiseases(setDiseases);
    
    })
    
    const handleDiseaseChange = (event) => {
        console.log(event.target.value);
        onDiseaseSelect(event.target.value);
      };

    return (
        <div>
            <InputSelect
                handleChange={handleDiseaseChange}
                options={diseases}
                text={text}
            ></InputSelect>
        </div>
    );    
  
};

export default DiseaseSelect;