class Pessoa:

    # ----------------------------------------------------------------------
    # Atributos
    __cpf   = None
    __nome  = None
    __email = None

    # ----------------------------------------------------------------------
    # Método Construtor
    def __init__(self, cpf:str, nome:str, email:str):
        self.__cpf   = cpf
        self.__nome  = nome
        self.__email = email

    def __init__(self):
        pass
    
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

    @CPF.setter
    def CPF(self, cpf):
        self.__cpf = cpf

    @Nome.setter
    def Nome(self, nome):
        self.__nome = nome
                        
    @Email.setter
    def Email(self, email):
        self.__email = email
