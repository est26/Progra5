from fastapi import FastAPI, HTTPException

app = FastAPI(title="API Proveedor de Madera (Simulada)")


inventario_madera = {
    "cedro": {"precio_m3": 185000, "disponible": True, "stock_m3": 42, "tiempo_entrega_dias": 5},
    "pino":  {"precio_m3": 95000,  "disponible": True, "stock_m3": 78, "tiempo_entrega_dias": 3},
    "roble": {"precio_m3": 260000, "disponible": True, "stock_m3": 15, "tiempo_entrega_dias": 10},
    "caoba": {"precio_m3": 310000, "disponible": False, "stock_m3": 0, "tiempo_entrega_dias": None},
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