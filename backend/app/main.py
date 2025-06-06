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