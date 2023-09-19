class Pessoa:        

    # --------------------------------------------------------------------------------
    # Declarando os atributos
    __cpf   = None
    __nome  = None
    __email = None
    __dados = None

    # --------------------------------------------------------------------------------
    # Obtendo os atributos
    @property
    def dados(self):
        return self.__dados

    # --------------------------------------------------------------------------------
    def __init__(self, cpf: str, nome: str, email: str):
        self.__cpf   = cpf
        self.__nome  = nome
        self.__email = email
        self.__dados = {cpf: {'CPF': self.__cpf , 'nomePessoa': self.__nome, 'emailPessoa': self.__email}}



