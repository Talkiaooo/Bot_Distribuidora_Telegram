# ia.py
def clasificar_intencion(mensaje):
    msg = mensaje.lower()
    # Puntuación por intenciones
    scores = {
        "ver_promos": len([w for w in ["promo", "oferta", "descuento"] if w in msg]),
        "ver_productos": len([w for w in ["catalogo", "lista", "productos", "comprar"] if w in msg])
    }
    # Retorna la intención con mayor puntuación si supera un umbral
    mejor_intencion = max(scores, key=scores.get)
    return mejor_intencion if scores[mejor_intencion] > 0 else "desconocido"