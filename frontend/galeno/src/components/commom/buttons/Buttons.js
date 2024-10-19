import React from "react";
import style from './Buttons.module.css'

export function NormalButton ({text, onClickCallback}){
    return(
        <button className={style.NormalButton} onClick={onClickCallback}>{text}</button>
    )
}