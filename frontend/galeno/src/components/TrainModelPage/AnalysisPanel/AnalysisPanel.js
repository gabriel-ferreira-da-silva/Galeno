import React, { useEffect, useState } from "react";
import { fetchModelByName, sendTrainData } from "../../../services/commomServices";
import style from "./style.module.css";
import {FourSquare} from "react-loading-indicators"
import { Atom } from "react-loading-indicators";
import Fade from "react-reveal/Fade"

function AnalysisPanel({ loading, img, boxplots, distribuitions }) {
    useEffect(()=>{
        console.log(loading)
    },[])

    return (
        <div>
            {
                loading &&
                    <div className={style.container}>
                    {img ?
                        <div className={style.imageHolder}>
                            <Fade bottom duration={1000}>
                            <div className={style.title}> correlation </div>
                            <img className={style.corrimage} src={img} alt="Correlation Heatmap" />
                            </Fade>
                        </div>
                        
                        :
                            
                            loading ?
                            <div className={style.loadingHolder}>
                                <FourSquare color="#227fc3" size="medium" text="" textColor="" />
                            </div>
                            :
                            <div></div>
                        
                    }


                    {distribuitions.length > 0 ? 
                        <div className={style.imageHolder}>
                            <Fade bottom duration={1000}>
                            <div className={style.title}> distribuitions </div>
                            <div className={style.distHolder}>
                                {
                                distribuitions.map((dist, index) =>(
                                    
                                        <img  className={style.distimage} key={index} src={dist} alt={`Distribution ${index + 1}`} /> 
                                ))}
                            </div>
                            </Fade>
                        </div>
                    : (
                        loading ?
                            <div className={style.loadingHolder}>
                                <FourSquare color="#227fc3" size="medium" text="" textColor="" />
                            </div>
                            :
                            <div></div>
                    )}

                    {boxplots.length > 0 ? 
                        <div className={style.imageHolder}>
                            <Fade>
                            <div className={style.title}> boxplots</div>
                            <div className={style.distHolder}>
                                {
                                    boxplots.map((dist, index) => (
                                        <img className={style.distimage} key={index} src={dist} alt={`Distribution ${index + 1}`} />
                                    ))
                                }
                            </div>
                            </Fade>
                        </div>
                    : (
                        loading ?
                            <div className={style.loadingHolder}>
                                <FourSquare color="#227fc3" size="medium" text="" textColor="" />
                            </div>
                            :
                            <div></div>
                    )}
                </div>
            

            }
            
        </div>
    );
}

export default AnalysisPanel;
