import { useState } from "react";
import DiseaseSelect from "../components/FormsPage/DiseaseSelect/DiseaseSelect";
import ModelSelect from "../components/FormsPage/ModelSelect/ModelSelect";
import ModelForm from "../components/FormsPage/ModelForm/ModelForm";
import ResultsPanel from "../components/FormsPage/ResultsPanel/ResultsPanel";
import SelectsPanel from "../components/FormsPage/SelectPanel/SelectPanels";
function FormPage() {
  
  const [disease, selectDisease] = useState("");
  const [model, selectModel] = useState("");
  const [array,setArray] = useState([]);

  return (
    <div>
      <SelectsPanel
        selectDisease={selectDisease}
        selectModel={selectModel}
        disease={disease}
      ></SelectsPanel>

      <ModelForm
        model={model}
        disease={disease}
        setForm={setArray}
      />
      <ResultsPanel
        model={model}
        input={array}
      />
      
    </div>
    
  );
}

export default FormPage;
