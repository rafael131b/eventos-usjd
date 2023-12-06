# Services/UsuarioService.py
from Model.UsuarioModel import UsuarioModel
from DB.BancoDeDados import BancoDeDados

# Exemplo de uso da classe BancoDeDados
banco = BancoDeDados()

# Cria as tabelas no banco de dados
banco.criar_tabelas()
class UsuarioService:


    def __init__(self):
        self.usuarios = []


    def criar_usuario(self, idUsuario, nomeUsuario, cpfUsuario, emailUsuario, senhaUsuario):
        usuario = UsuarioModel(id=idUsuario, nome=nomeUsuario, cpf=cpfUsuario, email=emailUsuario, senha=senhaUsuario)
        self.usuarios.append(usuario)
        banco.inserir_usuario(nomeUsuario,cpfUsuario,emailUsuario)
        print(f"Usuário {nomeUsuario} criado com sucesso.")

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

    def obter_evento_por_id(self, id_evento):
        print(f"Evento com ID {id_evento} não encontrado.")
        return None
