import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1/config-checker';


export const checkNginxConfig = async (file: File): Promise<string> => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post('/check-config/', formData);
        return response.data;
    } catch (error: unknown) {
        if (error instanceof Error) {
            throw new Error('Ошибка при проверке конфигурации NGINX: ' + error.message);
        } else {
            throw new Error('Неизвестная ошибка при проверке конфигурации NGINX');
        }
    }
};

export const uploadNginxConfigFile = async (file: File) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post(API_URL + '/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        throw new Error('Ошибка при загрузке файла конфигурации NGINX: ' + error.message);
    }
};