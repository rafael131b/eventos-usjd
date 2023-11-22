from Models.EventoModel import EventoModel
from Models.UsuarioModel import UsuarioModel

from View.EventoView import EventoView
from Controller.EventoController import EventoController


# Criar instâncias
modelo = EventoModel()
visualizacao = EventoView()
controle = EventoController(modelo, visualizacao)

# Adicionar evento usando o controlador
controle.adicionar_evento(1, "Evento  Homenagem ao Pelé", "rua Vila Belmiro", "esporte", None, "Homenagem o Rei Pelé na VIla Belimiro")
#controle.adicionar_evento(2, "andre", "rua jose santos", "esporte", None, "sem detalhes")
# Exemplo de uso
controle.mostrar_detalhes_evento(2)


usuario = UsuarioModel(nome="Davi", idade=32, email="daviSantos@gmail.com", id=1)

controle.adicionar_usuario_ao_evento(1,usuario.nome)
print("todos eventos",controle.obter_todos_eventos())





