import regras


class Atividades:
    CATEGORIAS_VALIDAS = {"Cultura", "Extensão", "Ensino", "Pesquisa"}

    def __init__(self, nome: str, categoria: str, horas_reais: int, peso: float):
        self._nome = nome
        self._categoria = categoria
        self.horas_reais = horas_reais
        self._peso = peso


class Alunos:
    def __init__(self, nome: str, codigo: str, curso: str, nivel: str):
        self._nome = nome
        self.__codigo = codigo
        self._curso = curso
        self._nivel = nivel

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def _codigo(self):
        return self.__codigo

    @_codigo.setter
    def _codigo(self, value):
        self.__codigo = value

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, value):
        self._curso = value

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value):
        self._nivel = value

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def horas_reais(self):
        return self._horas_reais

    @property
    def peso(self):
        return self._peso

    @horas_reais.setter
    def horas_reais(self, value):
        if value <= 0:
            raise ValueError("Horas não podem ser negativas!")
        self._horas_reais = value

    @peso.setter
    def peso(self, value):
        if value <= 0:
            raise ValueError("Peso não pode ser negativas!")
        self._peso = value

    @property
    def horas_validas(self):
        return self.horas_reais * self.peso

    @categoria.setter
    def categoria(self, value):
        if value not in self.CATEGORIAS_VALIDAS:
            raise ValueError(
                f"Categoria inválida! Use uma destas: {self.CATEGORIAS_VALIDAS}")
        self._categoria = value
