В проекте используется база данных SQLite, база данных уже существует.
Для создания новой базы данных можно запустить python create_db.py

Для запуска программы использовать python main.py

Эндпойнты:

'/incidents' - для создания нового инцидента в БД

'/incidents/{stat}' - для получения списка инцидентов с заданным статусом stat

'incident_update/{id}' - для обновления инцидента с заданным id


Примеры:

curl -X 'POST' 'http://127.0.0.1:8000/incidents' -H 'Content-Type: application/json' -d '{"description": "point online n:8000/incidents' -H 'Content-Type: application/json' -d '{"description": "point not responding", "stat": "offline", "source": "operator", "datetime": "2025-11-07 10:30:00"}'

-- создание новой записи

curl -X 'PUT' 'http://127.0.0.1:8000/incident_update/1' -d "error" 

-- обновление статуса инцидента по id=1 
