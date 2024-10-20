import style from './style.module.css'
import DiseaseSelect from '../DiseaseSelect/DiseaseSelect';
import ModelSelect from '../ModelSelect/ModelSelect';

function SelectsPanel({selectDisease, selectModel,disease}) {
  return (
    <div>
      <p>Select disease and model to predict</p>
      <div className={style.panel}>
          <DiseaseSelect
            onDiseaseSelect={selectDisease}
          />
          
          <ModelSelect
            onModelSelect={selectModel}
            disease={disease}
          />
          
        </div>
    </div>
    
    
  );
}

export default SelectsPanel;
