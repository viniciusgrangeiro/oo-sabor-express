from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # significa que todas as classes derivadas dessa, terao que ter esse metodo
    # mas não necessariamente preciso escrever algo nesse metodo nessa classe
    @abstractmethod
    def aplicar_desconto(self):
        pass