from class_Pessoa import Pessoa

class Aluno:
   
    # --------------------------------------------------------------------------------
    # Declarando os atributos
    __matricula = None
    __codcurso  = None
    __campus    = None
    __pessoa    = None

    # --------------------------------------------------------------------------------
    # Obtendo os atributos
    @property
    def dados(self):
        return self.__pessoa.dados

    # --------------------------------------------------------------------------------
    def __init__(self, cpf: str, matricula: str, codcurso: str, campus: str, pessoa: Pessoa):
        self.__matricula = matricula
        self.__codcurso  = codcurso
        self.__campus    = campus
        self.__pessoa    = pessoa

        self.__pessoa.dados[cpf][self.__matricula] = {
            'matriculaAluno': self.__matricula,
            'codCurso': self.__codcurso,
            'campus': self.__campus
        }
