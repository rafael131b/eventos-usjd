# Services/EventoService.py
from Models.EventoModel import EventoModel

class EventoService:
    def __init__(self):
        self.eventos = []

    def criar_evento(self, idEvento, nomeEvento, endereco, categoria, horario, descricao):
        evento = EventoModel(id=idEvento, nome=nomeEvento, endereco=endereco, categoria=categoria, horario=horario, descricao=descricao)
        self.eventos.append(evento)
        print(f"Evento: {nomeEvento} FOI CRIADO COM SUCESSO")

    def obter_todos_eventos(self):
        return self.eventos

    def obter_evento_por_id(self, id_evento):
        for evento in self.eventos:
            print(f"ID do Evento: {evento.id}, ID procurado: {id_evento}")
            if evento.id == id_evento:
                return evento
        print(f"Evento com ID {id_evento} não encontrado.")
        return None

