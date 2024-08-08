from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cadapio = []
        Restaurante.restaurantes.append(self)

    @classmethod
    def listar_restaurantes(cls):
        for restaurente in cls.restaurantes:
            print(f'{restaurente._nome.ljust(18)} | '
                  f'{restaurente._categoria.ljust(18)} | '
                  f'{str(restaurente.media_avaliacoes).ljust(18)} | '
                  f'{restaurente.ativo}')

    @property
    def ativo(self):
        if self._ativo:
            return 'ativo'
        else:
            return 'desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'

        soma_avaliacoes = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_avaliacoes / quantidade_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cadapio.append(item)

    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cadapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = (f'{i}. Nome: {item.nome} | '
                                  f'Preco: R${item.preco} | Descricao: '
                                  f'{item.descricao}')
                print(mensagem_prato)
            else:
                mensagem_bebida = (f'{i}. Nome: {item.nome} | '
                                   f'Preco: R${item.preco} | Tamanho: '
                                   f'{item.tamanho}')
                print(mensagem_bebida)
