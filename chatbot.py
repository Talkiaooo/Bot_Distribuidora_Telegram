import json
import spacy

# Cargamos el modelo preentrenado de spaCy
nlp = spacy.load("es_core_news_sm")

with open('productos.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

def obtener_promos():
    promos = [p['descripcion'] for p in db.get('promociones_temporales', {}).values()]
    return "🔥 *Promos vigentes:*\n" + "\n".join([f"• {p}" for p in promos])

def obtener_lista_productos(cat):
    prods = [p for p in db.get('productos', {}).values() if p.get('categoria') == cat]
    if not prods: return "⚠️ No hay productos disponibles en esta categoría."
    lista = f"📦 *Catálogo - {cat.capitalize()}*\n\n"
    for p in prods:
        stock_msg = f"📊 Stock: {p['stock']}" if p['stock'] > 0 else "❌ SIN STOCK"
        lista += f"• {p['nombre']} | ${p['precio']} | {stock_msg}\n"
    return lista

def procesar_logica(mensaje, sesion):
    # FASE 1: Registro (Se mantiene igual)
    if sesion.get("estado") == "REGISTRO":
        paso = sesion.get("paso", "NOMBRE")
        if paso == "NOMBRE":
            sesion["datos"] = {"nombre": mensaje}
            sesion["paso"] = "EMPRESA"
            return "Perfecto. ¿De qué empresa nos contactás?"
        elif paso == "EMPRESA":
            sesion["datos"]["empresa"] = mensaje
            sesion["paso"] = "LOCALIDAD"
            return "¿Cuál es tu localidad?"
        elif paso == "LOCALIDAD":
            sesion["datos"]["localidad"] = mensaje
            sesion["estado"] = "ACTIVO"
            return "¡Gracias! Registro completado."

    # FASE 2: Clasificación con spaCy (Requisito PLN)
    doc = nlp(mensaje.lower())
    # Usamos lematización para entender la raíz de la palabra
    lemmas = [token.lemma_ for token in doc]
    
    if any(l in ["promo", "oferta", "descuento"] for l in lemmas):
        return "INTENCION_PROMOS"
    if any(l in ["menu", "producto", "catalogo", "lista"] for l in lemmas):
        return "INTENCION_MENU"
    
    # Similitud semántica para categorías
    for cat in ["bebidas", "almacen", "limpieza"]:
        if nlp(cat).similarity(doc) > 0.6:
            return f"INTENCION_CAT_{cat.upper()}"
            
    return None