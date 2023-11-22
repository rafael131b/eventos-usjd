class UsuarioController:
    @staticmethod
    def atualizar_email(usuario, novo_email):
        usuario.email = novo_email
