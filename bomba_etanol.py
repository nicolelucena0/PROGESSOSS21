from bomba_combustivel import BombaCombustivel

class BombaEtanol(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

# Testing

bomba = BombaEtanol(2, 100)
litros = bomba.abastecer_por_valor(2000)
print(litros)