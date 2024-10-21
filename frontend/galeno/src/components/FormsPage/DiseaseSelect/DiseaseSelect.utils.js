import { fetchAvailableDiseases } from '../../../services/commomServices';


export const loadAvailableDiseases = async (setDiseases) =>{
    const response = await fetchAvailableDiseases();
    setDiseases(response);
}
