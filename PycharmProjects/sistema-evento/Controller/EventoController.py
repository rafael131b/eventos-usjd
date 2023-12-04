from Services.EventoServices import EventoService

class EventoController:
    service = EventoService()

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def adicionar_evento(self):
        idEvento = input("Digite o ID do evento: ")
        nomeEvento = input("Digite o Nome do Evento: ")
        endereco = input("Digite o Endereço do Evento: ")
        categoria = input("Digite a Categoria do Evento: ")
        horario = input("Digite o Horário do Evento: ")
        descricao = input("Digite a Descrição do Evento: ")

        self.service.criar_evento(idEvento, nomeEvento, endereco, categoria, horario, descricao)

    def obter_todos_eventos(self):
        todos_eventos = self.service.obter_todos_eventos()

        if todos_eventos:
            print("Lista de Eventos:")
            for evento in todos_eventos:
                print(f"ID: {evento.id}, Nome: {evento.nome}, Categoria: {evento.categoria}")
        else:
            print("Não há eventos disponíveis.")

# Exemplo de uso
evento_controller = EventoController(model=None, view=None)

# Chame o método para obter todos os eventos
evento_controller.obter_todos_eventos()
