class EventoModel:
    def __init__(self):
        self.eventos = []

    def obter_evento_por_id(self, evento_id):
        for evento in self.eventos:
            if evento['id'] == evento_id:
                return evento
        return None
