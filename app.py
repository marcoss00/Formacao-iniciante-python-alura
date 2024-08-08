from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_preca = Restaurante('praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'mexicana')
restaurante_japones = Restaurante('Japa', 'japonesa')

suco = Bebida('Suco de Melancia', 5, 'Grande')
suco.aplicar_desconto()
paozinho = Prato('Paozinho', 2.0, 'O melhor')
paozinho.aplicar_desconto()
restaurante_preca.adicionar_no_cardapio(suco)
restaurante_preca.adicionar_no_cardapio(paozinho)


def main():
    restaurante_preca.exibir_cardapio()


if __name__ == '__main__':
    main()
