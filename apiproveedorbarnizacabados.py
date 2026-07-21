from fastapi import FastAPI, HTTPException

app = FastAPI(title="API Proveedor de Barniz/Acabados (Simulada)")


inventario_acabados = {
    "barniz": {"precio_litro": 12500, "disponible": True, "stock_litros": 60, "tiempo_entrega_dias": 4},
    "laca":   {"precio_litro": 15800, "disponible": True, "stock_litros": 35, "tiempo_entrega_dias": 6},
    "tinte":  {"precio_litro": 9800,  "disponible": True, "stock_litros": 50, "tiempo_entrega_dias": 3},
    "aceite": {"precio_litro": 18200, "disponible": False, "stock_litros": 0, "tiempo_entrega_dias": None},
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