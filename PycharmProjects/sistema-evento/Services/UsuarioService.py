from Models.UsuarioModel import UsuarioModel


class UsuarioService:
    def __init__(self, evento_service):
        self.usuarios = []
        self.evento_service = evento_service
    def criar_usuario(self, nome, idade, email, cpf):
        usuario = UsuarioModel(nome=nome, idade=idade, email=email, id=cpf)
        print(f"NOVO USUARIO CRIADO COM SUCESSO! {usuario.nome} está em nossa base de dados")
        return usuario

    def obter_todos_usuarios(self):
        return self.usuarios

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionar_evento_a_usuario(self, usuario, evento):
        if evento:
            usuario.eventos_associados.append(evento)
            print("Evento adicionado ao usuário.")

    def obter_usuario_por_cpf(self, cpf):

        for usuario in self.usuarios:
            if usuario.id == cpf:
                return usuario
        print(f"Usuário com CPF {cpf} não encontrado.")
        return None


    def adicionarEventoAoUsuario(self,evento):
        if evento:
         self.usuarios.append(evento)
         print("evento adicionado ao usuario")