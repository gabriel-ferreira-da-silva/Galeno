import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';
import { fetchDiseaseDescription } from '../../../services/commomServices';
import style from './style.module.css'

function DescriptionPanel({disease}){
    const [description, setDescription] = useState(null);

    useEffect(()=>{
        const getDescription = async (diseasename)=>{
            try{
                if((diseasename)==false) return;
                const response = await fetchDiseaseDescription(diseasename);
                setDescription(response[0]);
            }catch(e){
                setDescription(null)
            }
        }

        getDescription(disease);
    },[disease])

    return (
        <div className={style.container}>
            {
                disease ?
                <div className={style.container}>
                    <label className={style.title}>analyzis</label>
                    <div className={style.panel}>
                        {description}
                    </div>
                </div>

                :
                <div></div>

            }
        </div>
    );    
  
};

export default DescriptionPanel;