import React, { useState, useEffect } from 'react';
import { fetchModelsInputDescriptionByName } from '../../../services/commomServices';
import { NormalButton } from '../../commom/buttons/Buttons';
import style from './ModelForm.module.css';

import Fade from "react-reveal/Fade"

function ModelForm({ model, disease, setForm }) {
    const [inputs, setInputs] = useState([]);
    const [array, setArray] = useState([]);
    const [isVisible, setIsVisible] = useState(false); // State to manage visibility

    useEffect(() => {
        const fetchInputDescription = async (diseaseName) => {
            if (diseaseName === "") return;
            const response = await fetchModelsInputDescriptionByName(diseaseName);
            setInputs(response);
            setArray(new Array(response.length).fill(0));
        };

        fetchInputDescription(disease);
    }, [disease]);

    useEffect(() => {
        // Set visibility based on model
        if (model) {
            setIsVisible(true);
        } else {
            setIsVisible(false);
        }
    }, [model]);

    const updateArray = (event) => {
        const index = Number(event.target.name);
        const value = Number(event.target.value);

        setArray((prevArray) => {
            const newArray = [...prevArray];
            newArray[index] = value;
            return newArray;
        });
    };

    const submitArray = () => {
        setForm(array);
    };

    return (
        <div>
            {model && disease ? (
                <div>
                    <p>Fill the form</p>

                    <Fade bottom duration={1000}>
                        <div className={style.formPanel}>
                            {inputs.map((input, index) => (
                                <div key={index} className={style.inputHolder}>
                                    <label className={style.label}>{input}</label>
                                    <input
                                        name={index}
                                        className={style.input}
                                        onChange={updateArray}
                                    />
                                </div>
                            ))}
                        
                        <NormalButton
                            onClickCallback={submitArray}
                            text={"Submit"}
                        />
                        </div>
                        
                        
                    
                    </Fade>    
                </div>
            ) : (
                <div></div>
            )}
        </div>
    );
}

export default ModelForm;
