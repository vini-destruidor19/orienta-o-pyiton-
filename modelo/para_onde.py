class Para_onde:
    viagens = []
    def __init__(self,nome_passageira, localização_atual, destino):
        self.nome_passageira = nome_passageira
        self.localização_atual = localização_atual
        self.destino = destino
        self.ativo = False
        destino.viagens.append(self)

    def __str__(self):
        return f"{self.nome_passageira} | {self.localização_atual} | {self.destino} | {self.ativo}"

    def listar_destino():
        for destino in destino.viagens:
           print(f"{destino.nome_passageira} | {destino.localização_atual} | {destino.destino} ")

pessoa_alisson = Para_onde("alisson", "centro","morumbi")
pessoa_kauane = Para_onde("kauane", "morumbi","vila c")


para_onde = [pessoa_alisson, pessoa_kauane]

Para_onde.listar_destino()






