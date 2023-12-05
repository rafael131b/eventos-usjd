# Controller/UsuarioController.py
from Services.UsuarioService import UsuarioService
from Services.EventoServices import EventoService
from Controller.EventoController import  EventoController
class UsuarioController:
    def __init__(self, evento_service):
        self.service = UsuarioService(evento_service)
        self.evento_service = EventoService



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
                if usuario.eventos_associados:
                    print("Eventos Associados:")
                    for evento in usuario.eventos_associados:
                        print(
                            f"  - ID do Evento: {evento.id}, Nome do Evento: {evento.nome}, horario do Evento: {evento.horario}")
                else:
                    print("Usuário sem eventos associados.")
        else:
            print("Não há usuários disponíveis.")

    def obter_usuario_por_cpf(self):
        cpf = input("Digite o CPF do usuário: ")
        usuario = self.service.obter_usuario_por_cpf(cpf)

        if usuario:
            print(f"Usuário encontrado: Nome - {usuario.nome}, Idade - {usuario.idade}, Email - {usuario.email}, CPF - {usuario.id}")
        else:
            print(f"Usuário com CPF {cpf} não encontrado.")

    def adicionar_usuario_evento(self, evento):
        cpf = input("Digite o CPF do usuário: ")
        print("evento capturado",evento)
        usuario = self.service.obter_usuario_por_cpf(cpf)
        event






        if usuario:
            self.service.adicionar_evento_a_usuario(usuario, evento)
            print(f"Evento adicionado ao usuário {usuario.nome}.")


        else:
            print("Usuário não encontrado.")

