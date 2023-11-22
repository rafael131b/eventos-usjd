class EventoView:
    def mostrar_detalhes(self, evento):
        if evento:
            print(f"Detalhes do Evento: {evento}")
        else:
            print("Evento não encontrado.")
