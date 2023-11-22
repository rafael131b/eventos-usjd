class EventoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def adicionar_evento(self, evento_id, nome, endereco, categoria, horario, descricao):
        evento = {
            'id': evento_id,
            'nome': nome,
            'endereco': endereco,
            'categoria': categoria,
            'horario': horario,
            'descricao': descricao,
            'usuarios': []  # Lista de usuários associados ao evento
        }
        self.model.eventos.append(evento)

    def adicionar_usuario_ao_evento(self, evento_id, usuario):
        evento = self.model.obter_evento_por_id(evento_id)
        if evento:
            evento['usuarios'].append(usuario)
            print(f"Usuário adicionado ao evento com ID {evento_id}.")
        else:
            print(f"Evento com ID {evento_id} não encontrado.")

    def mostrar_detalhes_evento(self, evento_id):
        evento = self.model.obter_evento_por_id(evento_id)
        self.view.mostrar_detalhes(evento)

    def obter_todos_eventos(self):
        return self.model.eventos

    def excluir_evento(self, evento_id):
        evento = self.model.obter_evento_por_id(evento_id)
        if evento:
            self.model.eventos.remove(evento)
            print(f"Evento com ID {evento_id} excluído com sucesso.")
        else:
            print(f"Evento com ID {evento_id} não encontrado.")

    def atualizar_evento(self, evento_id, nome=None, endereco=None, categoria=None, horario=None, descricao=None):
        evento = self.model.obter_evento_por_id(evento_id)
        if evento:
            if nome:
                evento['nome'] = nome
            if endereco:
                evento['endereco'] = endereco
            if categoria:
                evento['categoria'] = categoria
            if horario:
                evento['horario'] = horario
            if descricao:
                evento['descricao'] = descricao

            print(f"Evento com ID {evento_id} atualizado com sucesso.")
        else:
            print(f"Evento com ID {evento_id} não encontrado.")
