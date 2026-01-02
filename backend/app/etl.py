import httpx
from .db import get_conn

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

def transform(payload: dict) -> list[dict]:
    cw = payload.get("current_weather") or {}
    # Nettoyage/casting simple
    return [{
        "timestamp": str(cw.get("time", "")),
        "temperature": float(cw["temperature"]) if "temperature" in cw else None,
        "windspeed": float(cw["windspeed"]) if "windspeed" in cw else None,
        "source": "open-meteo"
    }]

async def extract(lat: float, lon: float) -> dict:
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(OPEN_METEO_URL, params=params)
        r.raise_for_status()
        return r.json()

def load(rows: list[dict]) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO weather (timestamp, temperature, windspeed, source) VALUES (?, ?, ?, ?)",
        [(r["timestamp"], r["temperature"], r["windspeed"], r["source"]) for r in rows]
    )
    conn.commit()
    count = cur.rowcount
    conn.close()
    return count
