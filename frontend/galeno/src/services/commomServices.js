import axios from 'axios';

export const fetchAvailableDiseases = async ()=>{
    try {
        const response = await axios.get(`http://localhost:5000/api/diseases`);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};

export const fetchAllModels= async ()=>{
    try {
        const response = await axios.get(`http://localhost:5000/api/models/all`);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};

export const deleteModelByName = async (name)=>{
    try {
        const response = await axios.delete(`http://localhost:5000/api/models/byname/`+name);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};


export const sendTrainData = async (data) => {
    try {
        const response = await axios.post(
            'http://localhost:5000/api/models/analysedata', 
            data, 
            { headers: { 'Content-Type': 'multipart/form-data' } } // Explicitly set for clarity
        );
        return response.data;
    } catch (error) {
        console.error('Error posting training data to endpoint:', error);
        throw error;
    }
};

export const trainModel = async (data) => {
    try {
        const response = await axios.post(
            'http://localhost:5000/api/models/trainmodel', 
            data, 
            { headers: { 'Content-Type': 'multipart/form-data' } } // Explicitly set for clarity
        );
        return response.data;
    } catch (error) {
        console.error('Error posting training data to endpoint:', error);
        throw error;
    }
};


export const fetchModelByName = async(name)=>{
    try{
        const response = await axios.get(`http://localhost:5000/api/models/byname/`+name);
        return response.data
    }catch(error){
        throw error
    }
}
export const fetchAvailableModels = async ()=>{
    try{
        const response = await axios.get(`http://localhost:5000/api/models`);
        return response.data;
    } catch (error){
        console.error("error fetichin models" + error);
        throw error;
    }
}

export const fetchModelsNamesByDisease = async (disease)=>{
    try {
        const response = await axios.get(`http://localhost:5000/api/models/bydisease/`+disease);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};

export const fetchModelsInputDescriptionByName = async (name)=>{
    try {
        const response = await axios.get(`http://localhost:5000/api/diseases/inputdescription/`+name);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};



export const fetchDiseaseDescription = async (name)=>{
    try {
        const response = await axios.get(`http://localhost:5000/api/diseases/description/`+name);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};



export const fetchModelSchema = async ()=>{
    try {
        const response = await axios.get(`http://localhost:5000/api/models/schema`);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};


export const modelPredict = async (name,input)=>{
    try {
        const response = await axios.post(`http://localhost:5000/api/models/predict`, {
            name:name,
            input:input
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/diseases:', error);
        throw error;
    }
};

export const addNewModel = async (data)=>{
    try {
        const response = await axios.post(`http://localhost:5000/api/models/add`,data);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/models/add:', error);
        throw error;
    }
};


export const addNewDisease = async (data)=>{
    try {
        const response = await axios.post(`http://localhost:5000/api/diseases/add`,data);
        return response.data;
    } catch (error) {
        console.error('Error fetching avalilable diseases for endpoint http://localhost:5000/api/models/add:', error);
        throw error;
    }
};