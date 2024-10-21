import React, { useEffect } from "react";
import { useState } from "react";
import {fetchModelSchema } from "../../services/commomServices";

export default function ModelForm(){

    const [modelForm, setModelForm] = useState("");

    useEffect(()=>{
        const getModelForm = async()=>{
            try{
                const results  = await fetchModelSchema();
                setModelForm(results)
            }catch(error){
                console.log("error fetching diseases");
            }
        }
        getModelForm();
    },[]);

    return (
        <div>
            <h1>Model Schema</h1>
            {/* Handle loading state */}
            {modelForm === null ? (
                <p>Loading...</p>
            ) : (
                <pre>{JSON.stringify(modelForm, null, 2)}</pre>  // Format and display the schema
            )}
        <div>
            {Object.keys(modelForm).toString()}
        </div>
        </div>
        
    );
}