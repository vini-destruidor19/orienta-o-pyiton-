class Para_onde:
    viagens = []
    def __init__(self,nome_passageira, localização_atual, destino):
        self.nome_passageira = nome_passageira
        self.localização_atual = localização_atual
        self.destino = destino
        self._ativo = False
        Para_onde.viagens.append(self)

    def __str__(self):
        return f"{self.nome_passageira} | {self.localização_atual} | {self.destino} | {self.ativo}"

    def listar_destino():
        print("""𝑢𝑏𝑒𝑟\n""")
        print("__________________________________________________________________________________________")
        print(f"{"nome do passageiro".ljust(24)}| {"localização atual".ljust(20)} | {"destino".ljust(20)} | {"atatus"}")
        print("__________________________________________________________________________________________")

        for destino in Para_onde.viagens:
           print(f"{destino.nome_passageira.ljust(20)} | {destino.localização_atual.ljust(20)} | {destino.destino.ljust(20)} ")

    @property
    def ativo(self):
        return "⍨ Sem transporte disponivel" if self._ativo else "Ü Ativo"

pessoa_alisson = Para_onde("alisson", "centro","morumbi")
pessoa_kauane = Para_onde("kauane", "morumbi","vila c")


para_onde = [pessoa_alisson, pessoa_kauane]

Para_onde.listar_destino()






