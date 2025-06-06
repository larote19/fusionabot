from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FusionaBot API",
    version="0.1.0",
    description="API para detección y clasificación de necesidades de mercado"
)

# Permitir que el frontend se conecte a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta de prueba para saber si la API está viva
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok", "service": "fusionabot"}

from .services.mongo import db

@app.get("/db-status", tags=["health"])
async def db_status():
    try:
        # Verifica si puedes listar las colecciones
        collections = await db.list_collection_names()
        return {"status": "ok", "collections": collections}
    except Exception as e:
        return {"status": "error", "detail": str(e)}