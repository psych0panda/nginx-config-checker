import React, { useState } from 'react';

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

        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('/uploadfile/', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        onResult(result.message);
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
};

export default ConfigUploader;