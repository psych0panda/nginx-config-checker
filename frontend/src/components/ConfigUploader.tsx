import React, { useState } from 'react';
import {checkNginxConfig} from '../services/api';


interface ConfigUploaderProps {
    onResult: (result: string) => void;
}

const ConfigUploader: React.FC<ConfigUploaderProps> = ({ onResult }) => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setFile(event.target.files[0]);
        }
    };

    const handleUpload = async () => {
        if (!file) return;

        try {
            const response = await checkNginxConfig(file);
            onResult(response);
        } catch (error) {
            if (error instanceof Error) {
                onResult('Ошибка при загрузке: ' + error.message);
            } else {
                onResult('Неизвестная ошибка при загрузке файла конфигурации NGINX');
            }
        }
    };

    return (
        <div className='mt-4'>
            <div className='mb-3'>
                <input type="file" className='form-control' onChange={handleFileChange} />
            </div>
            <button className='btn btn-primary' onClick={handleUpload}>Upload</button>
        </div>
    );
};

export default ConfigUploader;