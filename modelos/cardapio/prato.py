from modelos.cardapio.item_cardapio import ItemCardapio

# Aqui estou dizendo que Prato ira herdar a classe ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # Aqui estou herdando esses atributos da superclass ItemCardapio
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome