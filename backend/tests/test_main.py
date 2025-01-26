import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def test_nginx_config():
    config_path = f"{os.getenv('BASE_DIR')}/tests/"
    print(f"Config path ===> {config_path}")
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    test_file = f"{config_path}/test_nginx.conf"
    with open(test_file, "w") as file:
        file.write(
            "user  nginx;\n"
            "worker_processes  auto;\n"
            "error_log  /var/log/nginx/error.log warn;\n"
            "pid        /var/run/nginx.pid;\n"
            "events {\n"
            "    worker_connections 1024;\n"
            "}\n"
            "http {\n"
            "    include       /etc/nginx/mime.types;\n"
            "    default_type  application/octet-stream;\n"
            "    log_format  main  '$remote_addr - $remote_user [$time_local] \"$request\" '\n"
            "                      '$status $body_bytes_sent \"$http_referer\" '\n"
            "                      '\"$http_user_agent\" \"$http_x_forwarded_for\"';\n"
            "    access_log  /var/log/nginx/access.log  main;\n"
            "    sendfile        on;\n"
            "    tcp_nopush      on;\n"
            "    tcp_nodelay     on;\n"
            "    keepalive_timeout  65;\n"
            "    types_hash_max_size 2048;\n"
            "    include /etc/nginx/conf.d/*.conf;\n"
            "}\n"
        )
    yield test_file
    os.remove(test_file)

def test_read_main():
    response = client.get("/docs")
    assert response.status_code == 200

def __str_to_bool(value: str) -> bool:
    return value.lower() in ["true", "1"]

def test_check_nginx_config(test_nginx_config):
    if __str_to_bool(os.getenv("IS_DOCKER")):
        with open(test_nginx_config, "rb") as file:
            response = client.post("/api/v1/config/check-config/", files={"file": file})
        print(response.content)
        assert response.status_code == 200
        assert response.json() == {"status": "success", "message": "Конфигурация корректна."}
    else:
        pytest.skip("По соображениям безопасности тест пропущен т.к. не был запущен в контейнере Docker.")