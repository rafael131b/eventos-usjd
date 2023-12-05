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

                if evento.listaUsuarios:
                    print("Usuários Associados:")
                    for usuario in evento.listaUsuarios:
                        print(f"  - Nome do Usuário: {usuario.nome}, CPF do Usuário: {usuario.id}")
                else:
                    print("Nenhum usuário associado a este evento.")
        else:
            print("Não há eventos disponíveis.")
    def obterEventoPorId(self):
        idInput=input("digite o id que vc quer encontrar")
        return self.service.obter_evento_por_id(self.model,idInput)

    def adicionar_evento_a_usuario(self, usuario,):
        idInput=input("digite o id que vc quer encontrar")
        evento= self.service.obter_evento_por_id(self.model, idInput)
        if evento and evento not in usuario.eventos_associados:
            self.service.adicionar_usuario_ao_evento(usuario)
            usuario.eventos_associados.append(evento)
            self.service.adicionar_usuario_ao_evento()
            print("Evento adicionado ao usuário.")
        else:
            print("Evento não válido ou já associado ao usuário.")


evento_controller = EventoController(model=None, view=None)


evento_controller.obter_todos_eventos()
