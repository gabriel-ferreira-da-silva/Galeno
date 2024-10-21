import React from "react";
import { useState } from "react";
import ModelForm from "../components/AddModelPage/ModelForm";
import SelectsPanel from "../components/FormsPage/SelectPanel/SelectPanels";

export default function AddModelPage(){

    const [disease, setDisease] = useState("")
    const [model, setModel] = useState("")

    return(
        <div>
            <SelectsPanel
            selectDisease={setDisease}
            selectModel={setModel}
            disease={disease}            
            ></SelectsPanel>
            <ModelForm>
                
            </ModelForm>
        </div>
    )
}