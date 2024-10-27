import React, { useEffect, useState } from "react";
import { fetchModelByName, sendTrainData } from "../../../services/commomServices";
import style from "./style.module.css";

function ModelPanel({ modelname, file, setFile }) {
    const [model, setModel] = useState(null);
    const [img, setImg] = useState(null);
    const [distribuitions, setDistribuitions] = useState([]); // Initialize as an empty array
    const [boxplots, setBoxplots] = useState([]); // Initialize as an empty array

    useEffect(() => {
        const fetchModel = async (name) => {
            try {
                const response = await fetchModelByName(name);
                setModel(response);
            } catch (error) {
                console.error("Error fetching model:", error);
            }
        };
        if (modelname) {
            fetchModel(modelname);
        }
    }, [modelname]);

    const handleChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append("traindata", file);

        try {
            const response = await sendTrainData(formData);
            setImg(`data:image/png;base64,${response.correlation}`);

            const newDistributions = response.distribuitions.map(
                (dist) => `data:image/png;base64,${dist}`
            );
            setDistribuitions(newDistributions); // Just set the state

            const newBoxplots = response.boxplots.map(
                (dist) => `data:image/png;base64,${dist}`
            );
            setBoxplots(newBoxplots); // Just set the state

            console.log(newDistributions.length);
        } catch (error) {
            console.error("Error loading image:", error);
        }
    };

    return (
        <div>
            {model ? (
                <div>
                    <div>
                        {"name: "}
                        {model.name}
                    </div>
                    <div>
                        {"type: "}
                        <div>{model.type}</div>
                    </div>
                    <div>
                        {"disease: "}
                        <div>{model.disease}</div>
                    </div>
                    <div>
                        {"description: "}
                        <div>{model.description}</div>
                    </div>
                    <div className={style.inputModelHolder}>
                        <div></div>
                        <label htmlFor="file-upload" className={style.fileInput}>
                            <div>Upload Data</div>
                        </label>
                        <input id="file-upload" type="file" onChange={handleChange} />

                        {file ? (
                            <div className={style.filetitle}>
                                <p>model: {file.name}</p>
                            </div>
                        ) : (
                            <div></div>
                        )}
                    </div>
                    <button className={style.NormalButton} onClick={handleSubmit}>
                        Submit
                    </button>

                    
                    {img && <img src={img} alt="Correlation Heatmap" />}

                    {distribuitions.length > 0 ? (
                        distribuitions.map((dist, index) => (
                            <img key={index} src={dist} alt={`Distribution ${index + 1}`} />
                        ))
                    ) : (
                        <div>Loading distributions...</div>
                    )}

                    {boxplots.length > 0 ? (
                        boxplots.map((dist, index) => (
                            <img key={index} src={dist} alt={`Distribution ${index + 1}`} />
                        ))
                    ) : (
                        <div>Loading distributions...</div>
                    )}
                </div>
            ) : (
                <div></div>
            )}
        </div>
    );
}

export default ModelPanel;
