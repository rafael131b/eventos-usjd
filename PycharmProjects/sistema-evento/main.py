from Models.EventoModel import EventoModel
from Models.UsuarioModel import UsuarioModel
from View.EventoView import EventoView
from Controller.EventoController import EventoController
from Controller.UsuarioController import UsuarioController
from Services.server import SimpleServer

modelo = EventoModel()
visualizacao = EventoView()
controle = EventoController(modelo, visualizacao)

controle.adicionar_evento(1, "Evento Homenagem ao Pelé", "rua Vila Belmiro", "esporte", None, "Homenagem o Rei Pelé na Vila Belmiro")

controle.mostrar_detalhes_evento(1)

def criar_usuario(nome, idade, email, cpf):
    print("Você deseja criar um Usuario")
    print(f"Nome: {nome}, Idade: {idade}, Email: {email}, CPF: {cpf}")
    usuario = UsuarioModel(nome=nome, idade=idade, email=email, id=cpf)
    print(f"NOVO USUARIO CRIADO COM SUCESSO! {usuario.nome} está em nossa base de dados")

def criar_evento():
    print("criar evento")
    idEvento=int(input("digite o ID"))
    nomeEvento = input("digite o Nome do Evento")
    endereco=input("digite o endereco")
    categoria=input("digite a categoria")
    horario=input("digite o horario")
    descricao = input("digite a descricao")
    controle.adicionar_evento(idEvento, nomeEvento, endereco, categoria, horario,descricao)
    print(f"Evento: {nomeEvento} FOI CRIADO COM SUCESSO")



def ver_eventos():
    pass

def ver_usuarios():
    # Implemente a lógica para ver todos os usuários aqui
    pass

print("Selecione o que você pretende fazer")
print("Digite 1 para criar um Usuario, digite 2 para criar um Evento, digite 3 para ver todos os eventos e digite 4 para ver todos usuarios")
valor_input = int(input())

if valor_input == 1:
    nome = input("Digite o Nome do Usuário que deseja criar: ")
    idade = int(input("Digite a Idade: "))
    email = input("Digite o Email: ")
    cpf = input("Digite o CPF: ")
    criar_usuario(nome, idade, email, cpf)
elif valor_input == 2:
    criar_evento()
elif valor_input == 3:
    ver_eventos()
elif valor_input == 4:
    ver_usuarios()
else:
    print("Opção inválida")
