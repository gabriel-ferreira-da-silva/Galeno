import React from "react";
import { useState } from "react";
import ModelsSelect from "../components/TrainModelPage/ModelsSelect/ModelsSelect";
import ModelPanel from "../components/TrainModelPage/ModelPanel/ModelPanel";

export default function TrainModelPage(){

    const [disease, setDisease] = useState("")
    const [model, setModel] = useState("")

    return(
        <div>
            <ModelsSelect
                onModelSelect={setModel}
            ></ModelsSelect>
            <ModelPanel
                modelname={model}
            ></ModelPanel>
        </div>
    )
}