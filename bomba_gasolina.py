from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    ADITIVO_PERCENTUAL = 0.05  # 5% de aditivo

    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

    def abastecer_por_valor_com_aditivo(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")
        
        valor_com_aditivo = self._valor_litro * (1 + self.ADITIVO_PERCENTUAL)
        litros = valor / valor_com_aditivo
        if litros > self._quantidade_disponivel:
            return -1
        
        self._quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro_com_aditivo(self, litros):
        if litros <= 0:
            raise ValueError("A quantidade de litros deve ser positiva")
        
        valor_com_aditivo = self._valor_litro * (1 + self.ADITIVO_PERCENTUAL)
        valor = litros * valor_com_aditivo
        if litros > self._quantidade_disponivel:
            return -1

# Testing


bomba = BombaGasolina(2, 100)
litros = bomba.abastecer_por_valor(2000)
print(litros)