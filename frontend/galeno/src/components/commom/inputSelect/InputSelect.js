import React from "react";
import style from './InputSelect.module.css'


function InputSelect({handleChange, options}){
    return(

        <div>
           <label>Select the disease you want diagnosis for: </label>

            <div>
                <select className={style.galSelect} onChange={handleChange}>
                    <option className={style.galOption} value={""} selected>---------</option>
                    {   
                        options.map((option, index)=>(
                            <option className={style.galOption}  key={index} value={option}>{option}</option>
                        ))
                    }
                </select>
            </div>
        </div>
    )
}

export default InputSelect;