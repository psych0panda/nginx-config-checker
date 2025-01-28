import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1/config/check-config/';


export const checkNginxConfig = async (file: File): Promise<string> => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post(API_URL, formData);
        return response.data;
    } catch (error: unknown) {
        if (error instanceof Error) {
            throw new Error('Ошибка при проверке конфигурации NGINX: ' + error.message);
        } else {
            throw new Error('Неизвестная ошибка при проверке конфигурации NGINX');
        }
    }
};
