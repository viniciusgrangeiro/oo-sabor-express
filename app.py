from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Fulan', 5)

def main():
    Restaurante.lista_restaurante()

if __name__ == '__main__':
    main()