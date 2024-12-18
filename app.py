from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'japonesa')

restaurante_mexicano.alternar_status()

def main():
    Restaurante.lista_restaurante()

if __name__ == '__main__':
    main()