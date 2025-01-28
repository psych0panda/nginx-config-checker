import React, { useState } from 'react';
import ConfigUploader from './components/ConfigUploader';

const App: React.FC = () => {
    const [result, setResult] = useState<string | null>(null);

    const handleResult = (result: string) => {
        setResult(result);
    };

    return (
        <div className="container mt-5">
            <h1 className="text-center">Проверка конфигурации NGINX</h1>
            <ConfigUploader onResult={handleResult} />
            {result && (
                <div className='mt-4'>
                    <h2>Результат проверки:</h2>
                    <p>{result}</p>
                </div>
            )}
        </div>
    );
};

export default App;