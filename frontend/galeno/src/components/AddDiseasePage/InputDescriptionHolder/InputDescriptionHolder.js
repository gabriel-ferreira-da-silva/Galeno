import React from "react";
import style from "./style.module.css"
function InputDescriptionHolder({ name, mainValue, descriptionValue, onMainChange, onDescriptionChange }) {
    return (
        <div className={style.inputHolder}>
            <div >Input:</div>
            <input
                name={`${name}-main`}
                value={mainValue}
                onChange={onMainChange}
            />
            <div>Description:</div>
            <input
                name={`${name}-description`}
                value={descriptionValue}
                onChange={onDescriptionChange}
            />
        </div>
    );
}

export default InputDescriptionHolder;
