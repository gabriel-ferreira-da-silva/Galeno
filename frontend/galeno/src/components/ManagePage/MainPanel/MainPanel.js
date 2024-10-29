import React, { useEffect, useState } from "react";
import ModelPanel from "../modelPanel/ModelPanel";
import { fetchAllModels } from "../../../services/commomServices";
import Fade from "react-reveal/Fade"
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
            <h1>Avalilable Models</h1>
            {models.map((model, index) => (
                <Fade bottom duration={1000}>
                    <div key={index}>
                        <ModelPanel
                            name={model.name}
                            description={model.description}
                            disease={model.disease}
                            type={model.type}
                        />
                    </div>
                </Fade>
            ))}
        </div>
    );
}

export default MainPanel;
