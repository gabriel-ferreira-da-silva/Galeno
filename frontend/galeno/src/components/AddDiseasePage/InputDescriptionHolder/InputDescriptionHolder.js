import React from "react";

function InputDescriptionHolder({ name, mainValue, descriptionValue, onMainChange, onDescriptionChange }) {
    return (
        <div>
            <div>Input:</div>
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
