class BancoDeDados:
    def __init__(self, nome_do_arquivo='dados.txt'):
        self.nome_do_arquivo = nome_do_arquivo

    def verificar_cpf_existente(self, cpf):
        with open(self.nome_do_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if linha.startswith('Usuario:'):
                    partes = linha.split(', ')
                    cpf_existente = partes[-1].split(': ')[1].strip()
                    if cpf_existente == cpf:
                        return True
        return False


    def criar_tabelas(self):
        # Não é necessário para salvar em arquivo de texto
        pass

    def inserir_usuario(self, nome, email, cpf,id_usuario):
        if self.verificar_cpf_existente(cpf):
            print(f"Erro: CPF {cpf} já existe. Não é possível cadastrar o usuário.")
            return

        with open(self.nome_do_arquivo, 'a') as arquivo:
            arquivo.write(f'Usuario: ID: {id_usuario}, Nome: {nome}, CPF: {cpf}, Email: {email}\n')


    def inserir_evento(self, nome_evento, endereco, categoria, horario, descricao):
        with open(self.nome_do_arquivo, 'a') as arquivo:
            arquivo.write(f'Evento: Nome: {nome_evento}, Endereço: {endereco}, Categoria: {categoria},'
                          f' Horário: {horario}, Descrição: {descricao}\n')

    def imprimir_usuarios(self):
        with open(self.nome_do_arquivo, 'r') as arquivo:
            print('\nLista de Usuários:')
            for linha in arquivo:
                if linha.startswith('Usuario:'):
                    print(linha.strip())

    def imprimir_eventos(self):
        with open(self.nome_do_arquivo, 'r') as arquivo:
            print('\nLista de Eventos:')
            for linha in arquivo:
                if linha.startswith('Evento:'):
                    print(linha.strip())


#