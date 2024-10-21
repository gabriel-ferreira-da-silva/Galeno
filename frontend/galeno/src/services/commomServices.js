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

export const fetchModelsNamesByDisease = async (disease)=>{
    try {
        const response = await axios.get(`http://localhost:5000/api/models/`+disease);
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