class EventoModel:
    def __init__(self, id=None, nome=None, endereco=None, categoria=None, horario=None, descricao=None):
        self.eventos = []
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.categoria = categoria
        self.horario = horario
        self.descricao = descricao


