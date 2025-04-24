#Inicio
class Atividades:
    def __init__(self, nome: str, horas_reais: int, peso: float):
        self._nome = nome
        self.horas_reais = horas_reais
        self._peso = peso

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def horas_reais(self):
        return self._horas_reais

    @horas_reais.setter
    def horas_reais(self, value):
        if value < 0:
            raise ValueError("Horas não podem ser negativas!")
        self._horas_reais = value
        
        

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, value):
        self._peso = value

    @property
    def horas_validas(self):
        return self.horas_reais * self.peso


teste = Atividades("Filme", -12 , 2.0)
print(teste.horas_validas)


