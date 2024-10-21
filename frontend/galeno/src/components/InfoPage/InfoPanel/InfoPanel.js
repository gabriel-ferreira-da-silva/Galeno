import React from "react";
import galen from "../../../assets/galen.png";
import style from "./style.module.css"
import Fade from "react-reveal/Fade"
export default function InfoPanel(){
    return (
        <div>
            <Fade bottom duration={1000}>
                <div className={style.infoPanel}>
                    <div className={style.imgHolder}>
                        <img src={galen}></img>
                        <p>Aelius Galenus, ancient physician</p>
                    </div>

                    <div className={style.textHolder}>
                        <h1>Galeno API</h1>
                        <p>Galeno is an API for analyzing diseases and providing diagnoses based on statistical and machine learning models, fully responsive to CRUD operations. In addition to making predictions, it is also possible to train and add new models. Galeno is powered by Python Flask for backend services, MongoDB for data persistence, React for the interface, and a bit of Bash scripting to enhance functionality.</p> 
                        <p>The name Galeno is a homage to Aelius Galenus, or Galen of Pergamon. He was a Roman and Greek physician, surgeon, and philosopher, considered one of the most accomplished medical researchers of antiquity. Galen influenced the development of various scientific disciplines, including anatomy, physiology, pathology, pharmacology, and neurology, as well as philosophy and logic.</p>
                    </div>   
                </div>
            </Fade>
        </div>
    )
}
