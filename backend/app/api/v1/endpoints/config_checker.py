import os
import docker
from fastapi import APIRouter, UploadFile, File, HTTPException
from dotenv import load_dotenv

router = APIRouter()
client = docker.from_env()


@router.post("/check-config/")
async def check_nginx_config(file: UploadFile = File(...)):
    load_dotenv()
    base_dir = os.getenv('BASE_DIR', '/tmp')
    temp_file_path = f"{base_dir}/{file.filename}"
    with open(temp_file_path, "wb") as temp_file:
        content: bytes = await file.read()
        temp_file.write(content)
    
    try:
        container = client.containers.run(
            "nginx:latest",
            detach=True,
            command=f"nginx -t -c {temp_file_path}",
            ports={"80/tcp": 8080},
            remove=False
        )
        container.wait()
        logs = container.logs()
        container.remove()
        os.remove(temp_file_path)
        return {"status": "success", "message": f"{logs.decode()}"}
    except docker.errors.ContainerError as e:
        raise HTTPException(status_code=400, detail=e.stderr.decode())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_file_path):
            print("Удаление временного файла...")
            os.remove(temp_file_path)
