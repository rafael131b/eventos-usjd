# Controller/UsuarioController.py
from Services.UsuarioService import UsuarioService
from Services.EventoServices import EventoService

class UsuarioController:
    service = UsuarioService()
    evento_service = EventoService()

    @staticmethod
    def atualizar_email(usuario, novo_email):
        usuario.email = novo_email

    def criar_usuario(self):
        nome = input("Digite o Nome do Usuário: ")
        idade = int(input("Digite a Idade: "))
        email = input("Digite o Email: ")
        cpf = input("Digite o CPF: ")

        novo_usuario = self.service.criar_usuario(nome, idade, email, cpf)
        self.service.adicionar_usuario(novo_usuario)
        print("Usuário adicionado à camada de controle.")

    def obter_todos_usuarios(self):
        todos_usuarios = self.service.obter_todos_usuarios()

        if todos_usuarios:
            print("Lista de Usuários:")
            for usuario in todos_usuarios:
                print(f"Nome: {usuario.nome}, Idade: {usuario.idade}, Email: {usuario.email}, CPF: {usuario.id}")
        else:
            print("Não há usuários disponíveis.")

    def adicionar_evento_a_usuario(self):
        cpf_usuario = input("Digite o CPF do usuário: ")
        id_evento = int(input("Digite o ID do evento: "))

        usuario = self.service.obter_usuario_por_cpf(cpf_usuario)
        evento = self.evento_service.obter_evento_por_id(id_evento)

        if usuario and evento:
            self.service.adicionar_evento_a_usuario(usuario, evento)
            print(f"Evento adicionado ao usuário {usuario.nome}.")
        else:
            print("Usuário ou evento não encontrado.")

    def obter_usuario_por_cpf(self, cpf):
        usuario = self.service.obter_usuario_por_cpf(cpf)


        if usuario:
            print(
                f"Usuário encontrado: Nome - {usuario.nome}, Idade - {usuario.idade}, Email - {usuario.email}, CPF - {usuario.id}")
        else:
            print(f"Usuário com CPF {cpf} não encontrado.")
