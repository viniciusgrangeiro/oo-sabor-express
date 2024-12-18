class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

# Exibe todos os metodos e atributos da classe
# print(dir(restaurante_praca))

# Exibe os atributos, com exceção do ativo
print(vars(restaurante_praca))