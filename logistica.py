# logistica.py
# Definimos zonas y sus días de demora adicionales según la distancia desde CP 5250
zonas_demora = {
    "local": 0,           # Santiago del Estero
    "cercana": 2,         # Provincias limítrofes
    "lejana": 5           # Resto del país
}

def calcular_envio_real(localidad_cliente):
    # Lógica de ejemplo: si la localidad es de Santiago, es inmediato
    if "santiago" in localidad_cliente.lower() or "ojo de agua" in localidad_cliente.lower():
        return f"Envío local (24hs)"
    return "Envío nacional (48-72hs)"