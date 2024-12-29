from modelos.restaurantes import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_praca = Restaurante('Praca', 'Gourmet')

bebida_melancia = Bebida('Suco de Melancia', 5.00, 'grande')
bebida_melancia.aplicar_desconto()
prato_pao = Prato('Pao', 2.00, 'O melhor pao da cicdade')
prato_pao.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(bebida_melancia)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()