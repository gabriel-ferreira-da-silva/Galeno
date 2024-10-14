import { useState } from "react";
import DiseaseSelect from "../components/DiseaseSelect/DiseaseSelect";
import ModelSelect from "../components/ModelSelect/ModelSelect";
function FormPage() {
  
  const [disease, selectDisease] = useState("");
  const [model, selectModel] = useState("");

  return (
    <div>
      <h1> this is form page</h1>
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

export default FormPage;
