import spacy
nlp = spacy.load("es_core_news_sm")
def extraer_intencion(texto):
    doc = nlp(texto.lower())
    lemmas = [t.lemma_ for t in doc]
    if any(l in lemmas for l in ["promo", "oferta"]): return "ver_promos"
    if any(l in lemmas for l in ["producto", "lista", "catálogo"]): return "ver_productos"
    return "desconocido"