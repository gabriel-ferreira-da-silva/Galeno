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
            <div className={style.panel}>
                <div>
                    <h2 className={style.title}>{name}</h2>
                    
                    <div className={style.holder}>
                        <p className={style.atributename}>Disease:</p>
                        <p className={style.atribute}>{disease}</p>
                    </div>

                    <div className={style.holder}>
                        <p className={style.atributename}>Type:</p>
                        <p className={style.atribute}>{type}</p>
                    </div>
                    <div className={style.holderdescription}>
                        <p className={style.atributename}>Description:</p>
                        <p className={style.atribute}>{description}</p>
                    </div>
                </div>
                <button className={style.deletebutton} onClick={handleDelete}>
                    delete
                </button>
            </div>
        );
    }

    export default ModelPanel;