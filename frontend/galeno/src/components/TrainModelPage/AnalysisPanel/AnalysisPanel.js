import React, { useEffect, useState } from "react";
import { fetchModelByName, sendTrainData } from "../../../services/commomServices";
import style from "./style.module.css";

function AnalysisPanel({ img, boxplots, distribuitions }) {
    return (
        <div>
            <div>
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
            
        </div>
    );
}

export default AnalysisPanel;
