import React, { useEffect, useState } from "react";
import { fetchModelByName, sendTrainData } from "../../../services/commomServices";
import style from "./style.module.css";
import Fade from "react-reveal/Fade"

function ModelPanel({ setLoading, modelname, file, setFile,setColumns,img,setImg,distribuitions, setDistribuitions,boxplots, setBoxplots}) {
    const [model, setModel] = useState(null);
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
        setLoading(true);
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
            setColumns(response.columns)

            console.log(newDistributions.length);
            
        } catch (error) {
            console.error("Error loading image:", error);
        }
    };

    return (
        <div>
            {model ? (
                <div>
                    <div className={style.container}>
                        <Fade bottom duration={1000}>
                        <div className={style.descriptors}>
                            <div className={style.labelholder}>
                                <div className={style.label}>{"Name: "}</div>
                                <div className={style.labeltext}>{model.name}</div>
                            </div>
                            <div className={style.labelholder}>
                                <div className={style.label}>{"Type: "}</div>
                                <div className={style.labeltext}>{model.type}</div>
                            </div>
                            <div className={style.labelholder}>
                                <div className={style.label}>{"Disease: "}</div>
                                <div className={style.labeltext}>{model.disease}</div>
                            </div>
                            <div clasName={style.labelholder}>
                                <div className={style.label}>{"Description: "}</div>
                                <div className={style.labeltext}>{model.description}</div>
                            </div>

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
                        </Fade>
                    </div>
                    <button className={style.NormalButton} onClick={handleSubmit}>
                        Submit
                    </button>
                </div>
            ) : (
                <div></div>
            )}
        </div>
    );
}

export default ModelPanel;
