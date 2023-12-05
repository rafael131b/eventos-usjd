# main.py
from Models.EventoModel import EventoModel
from View.EventoView import EventoView
from Controller.EventoController import EventoController
from Controller.UsuarioController import UsuarioController
from Services.EventoServices import EventoService

modelo = EventoModel()
visualizacao = EventoView()
controle = EventoController(modelo, visualizacao)
evento_service = EventoService()
usuarioController = UsuarioController(evento_service)

def executar():
    while True:
        print("Selecione o que você pretende fazer")
        print("Digite 1 para criar um Usuario, digite 2 para criar um Evento, digite 3 para ver todos os eventos e digite 4 para ver todos usuarios, digite 5 para adicionar um evento a um usuario e 6 para sair")
        valor_input = int(input())

        if valor_input == 1:
            usuarioController.criar_usuario()
        elif valor_input == 2:
            controle.adicionar_evento()
        elif valor_input == 3:
            controle.obter_todos_eventos()
        elif valor_input == 4:
            usuarioController.obter_todos_usuarios()
        elif valor_input == 5:
            evento=controle.obterEventoPorId()
            usuarioController.adicionar_usuario_evento(evento)


        elif valor_input == 6:
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

executar()
