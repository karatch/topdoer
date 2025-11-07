import uvicorn
from fastapi import FastAPI, Body, HTTPException, status
from typing import Annotated
from models import Incident
from connect_db import get_db_connection, DB_NAME

app = FastAPI()


@app.post('/incidents')
async def create(incident: Incident) -> dict:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        f'INSERT INTO {DB_NAME} (description, stat, source, datetime) VALUES (?, ?, ?, ?)',
        (incident.description, incident.stat, incident.source, incident.datetime,)
    )
    conn.commit()
    conn.close()
    return {'message': 'incident added successfully'}


@app.get('/incidents/{stat}')
async def read(stat: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM {DB_NAME} WHERE stat=?", (stat,)
    )
    data = cursor.fetchall()
    conn.close()
    return data


@app.put('/incident_update/{id}')
async def update(id: int, stat: Annotated[str, Body()]):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"""UPDATE {DB_NAME}
            SET stat=?
            WHERE id=?""", (stat, id))
    conn.commit()
    cursor.execute(f'SELECT * FROM {DB_NAME} WHERE id=?', (id,))
    if cursor.fetchone() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'incident {id} does not exist'
        )
    return {'message': f'incident {id} updated'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)