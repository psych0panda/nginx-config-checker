interface NginxConfig {
    content: string;
    isValid: boolean;
    errors?: string[];
}

interface ApiResponse {
    success: boolean;
    message: string;
    data?: NginxConfig;
}

export {};