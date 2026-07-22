from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="API Proveedor de Maquinaria (Simulada)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

maquinaria = {
    "sierra_circular": {"nombre": "Sierra circular de mesa", "precio": 450000, "disponible": True, "stock": 5, "garantia_meses": 12},
    "cepilladora":     {"nombre": "Cepilladora eléctrica", "precio": 680000, "disponible": True, "stock": 3, "garantia_meses": 24},
    "lijadora_banda":  {"nombre": "Lijadora de banda", "precio": 210000, "disponible": True, "stock": 8, "garantia_meses": 12},
    "torno_madera":    {"nombre": "Torno para madera", "precio": 890000, "disponible": False, "stock": 0, "garantia_meses": 24},
    "router_cnc":      {"nombre": "Router CNC para madera", "precio": 3200000, "disponible": True, "stock": 1, "garantia_meses": 36},
}

class SolicitudCotizacion(BaseModel):
    codigo: str
    cantidad: int

@app.get("/proveedor/maquinaria")
def listar_maquinaria():
    return maquinaria

@app.get("/proveedor/maquinaria/{codigo}")
def consultar_maquina(codigo: str):
    item = maquinaria.get(codigo)
    if not item:
        raise HTTPException(status_code=404, detail="Máquina no encontrada en el catálogo del proveedor")
    return {"codigo": codigo, **item}

@app.post("/proveedor/maquinaria/cotizar")
def cotizar_maquina(solicitud: SolicitudCotizacion):
    item = maquinaria.get(solicitud.codigo)
    if not item:
        raise HTTPException(status_code=404, detail="Máquina no encontrada")
    if not item["disponible"] or item["stock"] < solicitud.cantidad:
        raise HTTPException(status_code=400, detail="Stock insuficiente para esa cantidad")

    return {
        "codigo": solicitud.codigo,
        "cantidad": solicitud.cantidad,
        "total": item["precio"] * solicitud.cantidad,
        "tiempo_entrega_dias": 15,
        "estado": "COTIZACION_GENERADA"
    }
