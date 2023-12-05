# Services/EventoService.py
from Models.EventoModel import EventoModel

class EventoService:
    def __init__(self):
        self.eventos = []
        self.listaUsuarios=[]

    def criar_evento(self, idEvento, nomeEvento, endereco, categoria, horario, descricao):
        evento = EventoModel(id=idEvento, nome=nomeEvento, endereco=endereco, categoria=categoria, horario=horario, descricao=descricao)
        self.eventos.append(evento)
        print(f"Evento: {nomeEvento} FOI CRIADO COM SUCESSO")

    def obter_todos_eventos(self):
        return self.eventos

    def obter_evento_por_id(self, evento,idInput):
        for evento in self.eventos:
            print(f"ID do Evento: {evento.id}, ID procurado: {evento.id}")
            if evento.id == idInput:
                print("evento",evento)
                print("fodaaaaaa")

                return evento
        print(f"Evento com ID {evento.id} não encontrado.")
        return None

    def adicionar_usuario_ao_evento(self, usuario):
        self.service.adicionar_evento_a_usuario(usuario, self)
        print("Usuário adicionado com sucesso ao evento.")


