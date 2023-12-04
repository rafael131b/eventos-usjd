# Models/UsuarioModel.py
class UsuarioModel:
    def __init__(self, nome, idade, email, id):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.id = id
        self.eventos_associados = []  # Lista para armazenar eventos associados ao usuário
