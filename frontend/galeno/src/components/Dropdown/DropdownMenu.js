import React from 'react'; 
import {Dropdown} from 'rsuite';
import 'rsuite/dist/rsuite.min.css';
import style from './style.module.css'

function DropdownMenu() { 
	return ( 
		<div className={style.panel}>
			<Dropdown title={"title"} style={{ 
                    width: 200, 
                    border: '1px solid #ddd',
                    backgroundColor: 'black'
                }} 
            className={style.panel}> 
				<Dropdown.Item>Database</Dropdown.Item>
			</Dropdown> 
		</div> 
	) 
} 

export default DropdownMenu;
