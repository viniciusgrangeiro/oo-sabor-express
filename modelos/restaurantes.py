from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    # Cria uma instancia que recebe as informações do restaurante como parametro
    def __init__(self, nome, categoria): 
        self._nome = nome.title() # Todos os nomes com letra maiuscula na primeira letra
        self._categoria = categoria
        self._ativo = False # _ Informa que o atributo não foi setado pelo usuario
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    # Toda vez que fomos printar uma instancia, ele ira apresentar os Strings dessa instancia
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    

    @classmethod 
    def lista_restaurante(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    # Altera a forma com que determinada informação sera impressa
    # ao inves de imprimir False ou True, ele imprime os simbolos que eu pedi
    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    
    # Criamos dentro do property pois ele é um metodo para os objetos e não para a classe
    def alternar_status(self):
        self._ativo = not self._ativo


    # Essa função recebe uma avaliação de um cliente e uma nota e cria um objeto Avaliacao,
    # que sera guardado na lista de avaliacao de um objeto Restaurante
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    # O @property faz com que essa função se torne um atributo, sendo assim
    # podemos chama-lo como um atributo e apresentar as informações que estao contidas nele

    # como por exemplo a area de um retangulo:
    # class Retangulo:
    #     def __init__(self, altura, largura):
    #         self.altura = altura
    #         self.largura = largura
        
    #     --> Sem @property
    #         def calcula_area(self, altura, largura):
    #             return self.altura * self.largura
            
    #         retangulo = Retangulo(5,3)
    #         area = retangulo.calcula_area()
    #         print(area)
        
    #         --> saida: 15
        
    #     --> Com @property
    #         @property
    #         def calcula_area(self, altura, largura):
    #             return self.altura * self.largura
        
    #         retangulo = Retangulo(5,3)
    #         print(retangulo.calcula_area)
        
    #         --> saida: 15

    @property
    def media_avaliacoes(self):
        # Se não houver avaliações retorna 0
        if not self._avaliacao:
            return 0 
        
        # Soma cada nota de avaliacao deste objeto
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media_das_notas = round(soma_das_notas / quantidade_de_notas, 1)
        return media_das_notas