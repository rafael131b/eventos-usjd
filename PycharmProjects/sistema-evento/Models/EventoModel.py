class EventoModel:
    def __init__(self, id=None, nome=None, endereco=None, categoria=None, horario=None, descricao=None):
        self.eventos = []
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.categoria = categoria
        self.horario = horario
        self.descricao = descricao
        self.listaUsuarios=[]
    def __str__(self):
            return f"ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}, Categoria: {self.categoria}, Horário: {self.horario}, Descrição: {self.descricao}"

