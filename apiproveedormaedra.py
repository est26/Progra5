from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Proveedor de Madera (Simulada)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

inventario_madera = {
    "cipres":  {"precio_m3": 95000,  "disponible": True,  "stock_m3": 60, "tiempo_entrega_dias": 3},
    "laurel":  {"precio_m3": 130000, "disponible": True,  "stock_m3": 40, "tiempo_entrega_dias": 4},
    "cedro":   {"precio_m3": 185000, "disponible": True,  "stock_m3": 42, "tiempo_entrega_dias": 5},
    "teca":    {"precio_m3": 260000, "disponible": True,  "stock_m3": 15, "tiempo_entrega_dias": 10},
    "pochote": {"precio_m3": 310000, "disponible": False, "stock_m3": 0,  "tiempo_entrega_dias": None},
}

@app.get("/proveedor/madera")
def listar_madera():
    """Lista todos los tipos de madera que ofrece el proveedor."""
    return inventario_madera

@app.get("/proveedor/madera/{tipo}")
def consultar_madera(tipo: str):
    """Consulta un tipo de madera específico."""
    tipo = tipo.lower()
    info = inventario_madera.get(tipo)
    if not info:
        raise HTTPException(status_code=404, detail="Ese proveedor no maneja ese tipo de madera")
    return {"tipo": tipo, **info}
