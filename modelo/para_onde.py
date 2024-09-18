from modelo.Preco import Preco
class Para_onde:
    viagens = []
    def __init__(self,nome_passageira, localização_atual, destino):
        self._nome_passageira = nome_passageira.upper()
        self._localização_atual = localização_atual
        self._destino = destino
        self._preco = []
        self._ativo = False
        Para_onde.viagens.append(self)

    def __str__(self):
        return f"{self.nome_passageira} | {self.localização_atual} | {self.destino} | {self.ativo}"

    @classmethod
    def listar_destino(cls):
        print("""𝑢𝑏𝑒𝑟\n""")
        print("__________________________________________________________________________________________")
        print(f"{"nome do passageiro".ljust(24)}| {"localização atual".ljust(20)} | {"destino".ljust(20)} | {"estado da viagem".ljust(20)} | {"Preço Medio"}")
        print("__________________________________________________________________________________________")

        for destino in cls.viagens:
           print(f"{destino._nome_passageira.ljust(20)} | {destino._localização_atual.ljust(20)} | {destino._destino.ljust(20)} | {destino.ativo.ljust(20)} | {destino.media_preco}")

    @property
    def ativo(self):
        return "⍨ Sem transporte disponivel" if self._ativo else "Ü Ativo"
    
    def altenativa_destino(self):
        self._ativo = not self._ativo

    def receber_Preco(self, rota, valor):
        preco = Preco(rota, valor)
        self._preco.append(preco)

    @property
    def media_preco(self):
        if not self._preco:
            return 0
        soma_valor = sum(Preco._valor for Preco in self._preco)
        Quantidade_Rotas = len(self._preco)
        media = round(soma_valor / Quantidade_Rotas, 1)
        return media







