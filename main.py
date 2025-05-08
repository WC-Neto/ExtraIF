import regras
from typing import List


class Atividade:
    CATEGORIAS_VALIDAS = {"Cultura", "Extensão", "Ensino", "Pesquisa"}

    def __init__(self, nome: str, categoria: str, horas_certificado: int, subcategoria: str = None):
        self._nome = nome
        self.categoria = categoria 
        self._horas_certificado = self._validar_horas(horas_certificado)
        self._subcategoria = subcategoria
        self._peso = self._buscar_peso()  

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        if value not in self.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoria inválida! Use uma destas: {self.CATEGORIAS_VALIDAS}")
        self._categoria = value

    def _validar_horas(self, horas: int) -> int:
        if horas <= 0:
            raise ValueError("Horas devem ser positivas!")
        return horas

    def _buscar_peso(self) -> float:
        for cat, dados in regras.REGRAS_SUPERIOR.items():
            if self._categoria in cat: 
                for subcat, valores in dados["subcategorias"].items():
                    if self._nome in subcat: 
                        return valores["peso"]
        raise ValueError("Atividade não encontrada nas regras!")

    @property
    def pontos(self) -> float:
        return self._horas_certificado * self._peso
    
    
class Aluno:
    CURSOS_VALIDOS = {"Análise de Sistemas", "Eletrotécnica", "Informática", "Automação industrial", "Engenharia da Computação", "Engenharia de controle e automação"}  
    NIVEIS_VALIDOS = {"Técnico", "Superior"}

    def __init__(self, nome: str, ra: str, curso: str, nivel: str):
        self.nome = nome 
        self.ra = ra      
        self.curso = curso  
        self.nivel = nivel  
        self.__horas_complementares = 0 

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value: str):
        if not value.strip():
            raise ValueError("Nome não pode ser vazio!")
        self._nome = value

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, value: str):
        if not value.strip() or len(value) != 5:  
            raise ValueError("RA inválido! Deve ter 5 caracteres.")
        self.__ra = value

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, value: str):
        if value not in self.CURSOS_VALIDOS:
            raise ValueError(f"Curso inválido! Opções: {self.CURSOS_VALIDOS}")
        self._curso = value

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, value: str):
        if value not in self.NIVEIS_VALIDOS:
            raise ValueError("Nível deve ser 'Técnico' ou 'Superior'!")
        self._nivel = value

    @property
    def horas_necessarias(self) -> int:
        return 275 if self.nivel == "Superior" else 150

    def adicionar_horas(self, atividade: Atividade):
        if atividade.pontos <= 0:
            raise ValueError("Atividade sem pontos válidos!")
        self.__horas_complementares += atividade.pontos

    @property
    def horas_completadas(self) -> int:
        return self.__horas_complementares

    def cumpriu_meta(self) -> bool:
        return self.horas_completadas >= self.horas_necessarias
    
class MenuAtividades:
    @staticmethod
    def escolher_atividade() -> Atividade:
        print("Atividades disponíveis:")
        for i, (cat, dados) in enumerate(regras.REGRAS_SUPERIOR.items(), 1):
            print(f"{i}. {cat}")
        escolha = int(input("Digite o número: "))
        

class Menu:
    def __init__(self):
        self.alunos = []  

    def exibir_menu(self):
        while True:
            try:
                opcao = input(''' 
                ---------------------
                Bem vindo ao ExtraIF
                Como podemos te ajudar?
                1. Cadastrar aluno
                2. Adicionar atividade
                3. Sair
                ---------------------
                Escolha uma opção: ''')
                
                if opcao == '1':
                    self.cadastrar_aluno()
                elif opcao == '2':
                    self.adicionar_atividade()
                elif opcao == '3':
                    print("Saindo do sistema. Até logo!")
                    break
                else:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

    def cadastrar_aluno(self):
        try:
            nome = input("Digite o nome do aluno: ").strip()
            ra = input("Digite o RA do aluno (5 caracteres): ").strip()
            curso = input(f"Digite o curso do aluno ({', '.join(Aluno.CURSOS_VALIDOS)}): ").strip()
            nivel = input(f"Digite o nível do aluno ({', '.join(Aluno.NIVEIS_VALIDOS)}): ").strip()

            aluno = Aluno(nome=nome, ra=ra, curso=curso, nivel=nivel)
            self.alunos.append(aluno)
            print(f"Aluno {nome} cadastrado com sucesso!")
        except ValueError as ve:
            print(f"Erro ao cadastrar aluno: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def adicionar_atividade(self):
        try:
            if not self.alunos:
                print("Nenhum aluno cadastrado. Cadastre um aluno primeiro.")
                return

            ra = input("Digite o RA do aluno para adicionar atividade: ").strip()
            aluno = next((a for a in self.alunos if a.ra == ra), None)

            if not aluno:
                print("Aluno não encontrado!")
                return

            nome_atividade = input("Digite o nome da atividade: ").strip()
            categoria = input(f"Digite a categoria da atividade ({', '.join(Atividade.CATEGORIAS_VALIDAS)}): ").strip()
            horas_certificado = int(input("Digite as horas do certificado: "))

            atividade = Atividade(nome=nome_atividade, categoria=categoria, horas_certificado=horas_certificado)
            aluno.adicionar_horas(atividade)
            print(f"Atividade '{nome_atividade}' adicionada com sucesso para o aluno {aluno.nome}!")
        except ValueError as ve:
            print(f"Erro ao adicionar atividade: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()
