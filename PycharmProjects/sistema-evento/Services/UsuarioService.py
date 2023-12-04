from Models.UsuarioModel import UsuarioModel


class UsuarioService:
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self, nome, idade, email, cpf):
        usuario = UsuarioModel(nome=nome, idade=idade, email=email, id=cpf)
        print(f"NOVO USUARIO CRIADO COM SUCESSO! {usuario.nome} está em nossa base de dados")
        return usuario

    def obter_todos_usuarios(self):
        return self.usuarios

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_evento_a_usuario(self, usuario, evento):
        evento_existente = self.obter_evento_por_id(evento.id)

        if evento_existente:
            if evento_existente not in usuario.eventos_associados:
                usuario.eventos_associados.append(evento_existente)
                print(f"Evento adicionado ao usuário {usuario.nome}")
            else:
                print(f"O usuário {usuario.nome} já está associado a este evento.")
        else:
            print(f"Evento com ID {evento.id} não encontrado.")

    def obter_usuario_por_cpf(self, cpf):
        print(" self.usuarios", self.usuarios)
        for usuario in self.usuarios:
            if usuario.id == cpf:
                return usuario
        print(f"Usuário com CPF {cpf} não encontrado.")
        return None

    def obter_evento_por_id(self, id_evento):
        for usuario in self.usuarios:
            for evento in usuario.eventos_associados:
                if evento.id == id_evento:
                    return evento

        # Se não encontrar em nenhum usuário, procurar diretamente nos eventos
        for evento in self.eventos:
            if evento.id == id_evento:
                return evento

        print(f"Evento com ID {id_evento} não encontrado.")
        return None
