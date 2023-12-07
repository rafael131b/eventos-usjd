# Services/UsuarioService.py
from Model.UsuarioModel import UsuarioModel
from DB.BancoDeDados import BancoDeDados
import random

# Exemplo de uso da classe BancoDeDados
banco = BancoDeDados()

# Cria as tabelas no banco de dados
banco.criar_tabelas()
class UsuarioService:
    id_counter = 1

    def __init__(self):
        self.usuarios = []

    def gerar_id_aleatorio(self):
        return random.randint(1, 999999)

    def cpf_existente(self, cpf):
        usuario_existente = self.obter_usuario_por_cpf(cpf)
        return usuario_existente is not None

    def criar_usuario(self, nomeUsuario, cpfUsuario, emailUsuario, senhaUsuario):
        if self.cpf_existente(cpfUsuario):
            print(f"Erro: CPF {cpfUsuario} já existe. Não é possível cadastrar o usuário.")
            return

        idUsuario = self.gerar_id_aleatorio()


        usuario = UsuarioModel(id=idUsuario, nome=nomeUsuario, cpf=cpfUsuario, email=emailUsuario, senha=senhaUsuario)
        self.usuarios.append(usuario)
        banco.inserir_usuario(nomeUsuario, cpfUsuario, emailUsuario,idUsuario)
        print(f"Usuário {nomeUsuario} criado com sucesso, ID: {idUsuario}.")

    def adicionar_evento_associado(self, usuario, evento_id):
        evento = self.obter_evento_por_id(evento_id)
        if evento:
            usuario.eventos_associados.append(evento)
            print(f"Evento {evento.nome} adicionado aos eventos associados do usuário {usuario.nome}.")
        else:
            print(f"Evento com ID {evento_id} não encontrado.")

    def obter_todos_usuarios(self):
        banco.imprimir_usuarios()

        return self.usuarios

    def obter_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        print(f"Usuário com ID {id_usuario} não encontrado.")
        return None

    def obter_usuario_por_cpf(self, cpf_usuario):
        for usuario in self.usuarios:
            if usuario.cpf == cpf_usuario:
                return usuario
        print(f"Usuário com CPF {cpf_usuario} não encontrado.")
        return None

