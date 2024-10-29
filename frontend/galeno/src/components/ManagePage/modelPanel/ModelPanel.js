    import React from "react";
    import style from './style.module.css'
    import { deleteModelByName } from "../../../services/commomServices";
    import { useEffect } from "react";

    function ModelPanel({name,description,type,disease}){
        
        const  handleDelete = async () => {
            try{
                const response = await deleteModelByName(name)
                console.log(response)
            }catch(error){
                console.log(error)
                throw error
            }
        }
        useEffect(()=>{
            console.log(name)
        },[])
        return(
            <div>
                <div>
                    <div>name: {name}</div>
                    <div>disease: {disease}</div>
                    <div>type: {type}</div>
                    <div>description: {description}</div>
                </div>
                <button onClick={handleDelete}>
                    delete
                </button>
            </div>
        );
    }

    export default ModelPanel;