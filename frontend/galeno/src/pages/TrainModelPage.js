import React from "react";
import { useState } from "react";
import ModelsSelect from "../components/TrainModelPage/ModelsSelect/ModelsSelect";
import ModelPanel from "../components/TrainModelPage/ModelPanel/ModelPanel";
import AnalysisPanel from "../components/TrainModelPage/AnalysisPanel/AnalysisPanel";
import SelectSubtmit from "../components/TrainModelPage/SelectAndSubmit/SelectSubmit";
export default function TrainModelPage(){

    const [disease, setDisease] = useState("")
    const [model, setModel] = useState("")
    const [file, setFile] = useState(null)
    const [img, setImg] = useState(null);
    const [distribuitions, setDistribuitions] = useState([]); // Initialize as an empty array
    const [boxplots, setBoxplots] = useState([]); 
    const [columns, setColumns] = useState([]);
    const [columTarget, setColumtarget] = useState([]);

    return(
        <div>
            <ModelsSelect
                onModelSelect={setModel}
            ></ModelsSelect>
            <ModelPanel
                modelname={model}
                file={file}
                setFile={setFile}
                img={img}
                setImg={setImg}
                boxplots={boxplots}
                setBoxplots={setBoxplots}
                distribuitions={distribuitions}
                setDistribuitions={setDistribuitions}
                setColumns={setColumns}               
            ></ModelPanel>
            <AnalysisPanel
                img={img}
                boxplots={boxplots}
                distribuitions={distribuitions}
            ></AnalysisPanel>
            <SelectSubtmit
                colums={columns}
                file={file}
                model={model}
                setColumtarget={setColumtarget}
                columTarget={columTarget}
            ></SelectSubtmit>
            
        </div>
    )
}