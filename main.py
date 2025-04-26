import regras
class Atividades:
    def __init__(self, nome: str,categoria: str, horas_reais: int, peso: float):
        self._nome = nome
        self._categoria = categoria
        self.horas_reais = horas_reais
        self._peso = peso

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


teste = Atividades("Filme", "Cultura", 12 , 2.0)
menu = input('''
      Bem vindo ao ExtraIF!
      Espero te ajudar a validar suas horas sem estresse!
      Qual seu tipo de curso?
      [1] Superior
      [2] Técnico
      ''')

