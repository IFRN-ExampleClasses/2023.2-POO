class Pessoa:

    # ----------------------------------------------------------------------
    # Atributos
    __cpf   = None
    __nome  = None
    __email = None

    # ----------------------------------------------------------------------
    # Método Construtor
    def __init__(self, cpf:str = None, nome:str = None, email:str = None):
        self.__cpf   = cpf
        self.__nome  = nome
        self.__email = email

    # ----------------------------------------------------------------------
    @property
    def CPF(self):
        return self.__cpf 

    @property
    def Nome(self):
        return self.__nome 

    @property
    def Email(self):
        return self.__email 

    # ----------------------------------------------------------------------
    @CPF.setter
    def CPF(self, cpf:str = Nome):
        self.__cpf = cpf

    @Nome.setter
    def Nome(self, nome:str = Nome):
        self.__nome = nome
                        
    @Email.setter
    def Email(self, email:str = Nome):
        self.__email = email
