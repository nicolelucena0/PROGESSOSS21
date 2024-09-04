class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self._valor_litro = valor_litro
        self._quantidade_disponivel = quantidade_disponivel

    def abastecer_por_valor(self, valor):
        litros = valor / self._valor_litro
        if litros > self._quantidade_disponivel:
            return -1
        
        self._quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        valor = litros * self._valor_litro
        
        if litros > self._quantidade_disponivel:
            return -1
        else:
            self._quantidade_disponivel -= litros
            return valor

    def get_valor_litro(self):
        return self._valor_litro

    def set_valor_litro(self, valor_litro):
        self._valor_litro = valor_litro

    def get_quantidade_disponivel(self):
        return self._quantidade_disponivel

    def set_quantidade_disponivel(self, quantidade_disponivel):
        self._quantidade_disponivel = quantidade_disponivel
        