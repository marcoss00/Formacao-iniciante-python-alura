from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    @abstractmethod
    def aplicar_desconto(self):
        pass
