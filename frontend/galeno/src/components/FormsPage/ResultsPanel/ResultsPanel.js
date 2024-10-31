    import React from 'react';
    import { useState } from 'react';
    import { useEffect } from 'react';
    import { modelPredict } from '../../../services/commomServices';
    import style from './style.module.css'
    import Fade from "react-reveal/Fade"


    function ResultsPanel({model, input}){
        const [results, setResults] = useState(null);
        const [res, setRes] = useState(null);
        const [description, setDescription] = useState(null);
        const [modelDescription, setModelDescription] = useState(null);

        useEffect(()=>{
            const predict = async (modelName,inputArray)=>{
                try{
                    if((modelName && inputArray)==false) return;
                    const response = await modelPredict(modelName,inputArray);
                    setResults(response);
                }catch(e){
                    setResults(null)
                }
            }

            if(model && input   ){
                predict(model,input);
            }
        },[model, input])

        useEffect(()=>{
            if(results){
                setRes(results.res);
                setDescription(results.output_description[0]);
                setModelDescription(results.model_description);
            }else{
                setRes(null);
                setDescription(null);
                setModelDescription(null);
            }
        },[results,model])
        return (
            <div className={style.container}>
                
                    {
                        results && model ?
                        <div className={style.container}>
                            <Fade bottom duration={1000}>
                                <label className={style.title}>Analyses</label>
                                <div className={style.panel}>
                                    
                                    <div className={style.text}> {model+" results"}
                                        <div>
                                            {"Diagnosis is : {" + res +"}"}
                                        </div>
                                        <div>
                                            {"Results interpretation:  " + description}
                                        </div>
                                    </div>
                                
                                    <div className={style.text}> Model Details 
                                        <div>{modelDescription}</div>
                                    </div>
                                </div>
                            </Fade>
                        </div>

                    :
                    <div></div>

                }
            </div>
        );    
    
    };

    export default ResultsPanel;