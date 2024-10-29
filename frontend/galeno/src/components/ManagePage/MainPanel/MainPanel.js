import React, { useEffect, useState } from "react";
import ModelPanel from "../modelPanel/ModelPanel";
import { fetchAllModels } from "../../../services/commomServices";

function MainPanel(){
    const [models, setModels] = useState([]);

    useEffect(() => {
        const getModels = async () => {
            try {
                const response = await fetchAllModels();
                console.log(response);
                setModels(response);    
            } catch (error) {
                console.log(error);
                throw error;
            }
        };

        getModels();
    }, []);
    
    return (
        <div>
            {models.map((model, index) => (
                <div key={index}>
                    <ModelPanel
                        name={model.name}
                        description={model.description}
                        disease={model.disease}
                        type={model.type}
                    />
                </div>
            ))}
        </div>
    );
}

export default MainPanel;
