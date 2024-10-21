import React from "react";
import { useState } from "react";
import ModelForm from "../components/AddModelPage/ModelForm";

export default function AddModelPage(){

    const [disease, setDisease] = useState("")
    const [model, setModel] = useState("")

    return(
        <div>
            <ModelForm>
                
            </ModelForm>
        </div>
    )
}