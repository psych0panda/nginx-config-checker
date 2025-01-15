import re
from fastapi import APIRouter, UploadFile, File, HTTPException
import subprocess
import os

router = APIRouter()

@router.post("/check-config/")
async def check_nginx_config(file: UploadFile = File(...)):
    try:
        base_dir = '/nginx-config-checker/backend'
        # Сохраняем загруженный файл во временное хранилище
        temp_file_path = f"{base_dir}/nginx/{file.filename}"
        print(temp_file_path)
        with open(temp_file_path, "wb") as temp_file:
            content = await file.read()
            temp_file.write(content)
        if not os.path.exists(temp_file_path):
            raise HTTPException(status_code=404, detail="Ошибка сохранения файла.")        

        # Проверяем структуру конфигурационного файла
        with open(temp_file_path, "r") as temp_file:
            config_content = temp_file.read()
            if not re.search(r'events\s*{', config_content):
                raise HTTPException(status_code=400, detail="Конфигурационный файл должен содержать блок 'events'.")
            if not re.search(r'http\s*{', config_content):
                raise HTTPException(status_code=400, detail="Конфигурационный файл должен содержать блок 'http'.")

        # Проверяем конфигурацию NGINX
        result = subprocess.run(
            ["nginx", "-t", "-c", temp_file_path, "-g", "pid /tmp/nginx.pid; daemon off;"],
            capture_output=True,
            text=True
        )

        # Удаляем временный файл
        os.remove(temp_file_path)

        if result.returncode == 0:
            return {"status": "success", "message": "Конфигурация корректна."}
        else:
            raise HTTPException(status_code=400, detail=result.stderr)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))