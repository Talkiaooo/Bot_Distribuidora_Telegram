class GestorMemoria:
    def __init__(self):
        self.sesiones = {}
    def obtener(self, chat_id):
        if chat_id not in self.sesiones:
            self.sesiones[chat_id] = {"estado": "REGISTRO", "paso": "NOMBRE", "datos": {}}
        return self.sesiones[chat_id]