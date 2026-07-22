from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Proveedor de Barniz/Acabados (Simulada)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

inventario_acabados = {
    "natural": {"precio_litro": 0,     "disponible": True, "stock_litros": 999, "tiempo_entrega_dias": 0},
    "barniz":  {"precio_litro": 12500, "disponible": True, "stock_litros": 60,  "tiempo_entrega_dias": 4},
    "laca":    {"precio_litro": 15800, "disponible": True, "stock_litros": 35,  "tiempo_entrega_dias": 6},
    "pintura": {"precio_litro": 9800,  "disponible": True, "stock_litros": 50,  "tiempo_entrega_dias": 3},
}

@app.get("/proveedor/acabados")
def listar_acabados():
    """Lista todos los tipos de acabado que ofrece el proveedor."""
    return inventario_acabados

@app.get("/proveedor/acabados/{tipo}")
def consultar_acabado(tipo: str):
    """Consulta un tipo de acabado específico."""
    tipo = tipo.lower()
    info = inventario_acabados.get(tipo)
    if not info:
        raise HTTPException(status_code=404, detail="Ese proveedor no maneja ese tipo de acabado")
    return {"tipo": tipo, **info}
