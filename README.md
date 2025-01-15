# NGINX Config Checker

Этот проект представляет собой приложение для проверки конфигурационных файлов NGINX с веб-интерфейсом на React и бэкендом на FastAPI.

## Структура проекта

Проект состоит из двух основных частей: бэкенда и фронтенда.

### Бэкенд

Бэкенд реализован с использованием FastAPI и включает в себя следующие файлы:

- **`backend/app/main.py`**: Точка входа для приложения FastAPI. Создает экземпляр приложения и настраивает маршруты.
- **`backend/app/api/v1/endpoints/config_checker.py`**: Конечная точка API для проверки конфигурационных файлов NGINX. Обрабатывает запросы на загрузку конфигурации и возвращает результаты проверки.
- **`backend/app/core/config.py`**: Настройки конфигурации приложения, такие как параметры окружения и настройки сервера.
- **`backend/app/models/__init__.py`**: Определения моделей данных, используемых в приложении (в данный момент пустой).
- **`backend/requirements.txt`**: Список зависимостей Python, необходимых для работы приложения.
- **`backend/README.md`**: Документация для бэкенда проекта.

### Фронтенд

Фронтенд реализован с использованием React и включает в себя следующие файлы:

- **`frontend/public/index.html`**: Основной HTML-шаблон для приложения React.
- **`frontend/src/App.tsx`**: Основной компонент приложения React.
- **`frontend/src/index.tsx`**: Точка входа для приложения React.
- **`frontend/src/components/ConfigUploader.tsx`**: Компонент для загрузки конфигурационного файла NGINX.
- **`frontend/src/services/api.ts`**: Функции для взаимодействия с API бэкенда.
- **`frontend/src/types/index.ts`**: Определения типов, используемых в приложении.
- **`frontend/package.json`**: Конфигурационный файл для npm.
- **`frontend/tsconfig.json`**: Конфигурационный файл для TypeScript.
- **`frontend/README.md`**: Документация для фронтенда проекта.

## Установка и запуск

1. Клонируйте репозиторий:
   ```
   git clone <URL_репозитория>
   cd nginx-config-checker
   ```

2. Установите зависимости для бэкенда:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Запустите бэкенд:
   ```
   uvicorn app.main:app --reload
   ```

4. Установите зависимости для фронтенда:
   ```
   cd frontend
   npm install
   ```

5. Запустите фронтенд:
   ```
   npm start
   ```

Теперь вы можете открыть приложение в браузере по адресу `http://localhost:3000`.