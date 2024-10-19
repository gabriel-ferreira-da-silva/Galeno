import style from './style.module.css'
import DiseaseSelect from '../DiseaseSelect/DiseaseSelect';
import ModelSelect from '../ModelSelect/ModelSelect';

function SelectsPanel({selectDisease, selectModel,disease}) {
  return (
    <div className={style.panel}>
      <DiseaseSelect
        onDiseaseSelect={selectDisease}
      />
      
      <ModelSelect
        onModelSelect={selectModel}
        disease={disease}
      />
      
    </div>
    
  );
}

export default SelectsPanel;
