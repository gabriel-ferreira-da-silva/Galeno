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