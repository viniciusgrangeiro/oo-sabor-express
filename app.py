from modelos.restaurantes import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_melancia = Bebida('Suco de Melancia', 5.0, 'grande')
prato_pao = Prato('Pao', 2.0, 'O melhor pao da cicdade')


def main():
    print(bebida_melancia)
    print(prato_pao)

if __name__ == '__main__':
    main()