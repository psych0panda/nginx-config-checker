import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import config_checker

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(config_checker.router, prefix="/api/v1/config", tags=["config"])

def is_docker_running():
    with open("/proc/1/cgroup", "r") as file:
        return "docker" in file.read()

# Вызов функции при запуске приложения и установка переменной окружения
if is_docker_running():
    os.environ["IS_DOCKER"] = "true"
    os.environ["BASE_DIR"] = "/app"
else:
    os.environ["IS_DOCKER"] = "false"
    current_path = os.path.abspath(__file__)
    backend_index = current_path.find('/backend/') + len('/backend/')
    base_dir = current_path[:backend_index]
    os.environ["BASE_DIR"] = base_dir