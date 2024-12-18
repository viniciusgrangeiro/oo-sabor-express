class Restaurante:
    restaurantes = []

    # Cria uma instancia que recebe as informações do restaurante como parametro
    def __init__(self, nome, categoria): 
        self._nome = nome.title() # Todos os nomes com letra maiuscula na primeira letra
        self._categoria = categoria
        self._ativo = False # _ Informa que o atributo não foi setado pelo usuario
        Restaurante.restaurantes.append(self)

    # Toda vez que fomos printar uma instancia, ele ira apresentar os Strings dessa instancia
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    

    @classmethod 
    def lista_restaurante(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    # Altera a forma com que determinada informação sera impressa
    # ao inves de imprimir False ou True, ele imprime os simbolos que eu pedi
    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    
    # Criamos dentro do property pois ele é um metodo para os objetos e não para a classe
    def alternar_status(self):
        self._ativo = not self._ativo
