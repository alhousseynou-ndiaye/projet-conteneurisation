from fastapi import FastAPI
from .db import init_db, get_conn
from .etl import extract, transform, load

app = FastAPI(title="ETL Backend")

@app.on_event("startup")
def _startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/etl/load")
async def etl_load(lat: float = 48.8566, lon: float = 2.3522):
    raw = await extract(lat, lon)
    rows = transform(raw)
    inserted = load(rows)
    return {"inserted": inserted, "sample": rows[0] if rows else None}

@app.get("/data")
def get_data(limit: int = 50):
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, timestamp, temperature, windspeed, source FROM weather ORDER BY id DESC LIMIT ?",
        (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.get("/version")
def version():
    return {"version": "1.0.0"}
