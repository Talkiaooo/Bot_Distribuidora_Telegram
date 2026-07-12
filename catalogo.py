import json

class Catalogo:
    def __init__(self):
        with open('productos.json', 'r', encoding='utf-8') as f:
            self.datos = json.load(f)