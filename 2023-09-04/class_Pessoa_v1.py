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
    # Métodos GET
    def get_CPF(self):
        return self.__cpf 

    def get_Nome(self):
        return self.__nome 

    def get_Email(self):
        return self.__email 
                        
    # ----------------------------------------------------------------------
    # Métodos SET
    def set_CPF(self, cpf:str = None):
        self.__cpf = cpf

    def set_Nome(self, nome:str = None):
        self.__nome = nome

    def set_Email(self, email:str = None):
        self.__email = email
