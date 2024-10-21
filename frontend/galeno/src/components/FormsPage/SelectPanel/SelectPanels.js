import style from './style.module.css'
import DiseaseSelect from '../DiseaseSelect/DiseaseSelect';
import ModelSelect from '../ModelSelect/ModelSelect';
import Fade from "react-reveal/Fade"

function SelectsPanel({selectDisease, selectModel,disease}) {
  return (
    <div>
      <Fade bottom duration={1000}>
        <p>Select disease and model to predict</p>
        <div className={style.panel}>
            <DiseaseSelect
              onDiseaseSelect={selectDisease}
              text={"select target disease: "}
            />
            
            <ModelSelect
              onModelSelect={selectModel}
              disease={disease}
            />
            
          </div>
      </Fade>
    </div>
    
    
  );
}

export default SelectsPanel;
