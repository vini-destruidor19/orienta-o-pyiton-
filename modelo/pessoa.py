class Para_onde:
    def __init__(self,nome_passageira, localização_atual, destino, ativo):
        self.nome_passageira = nome_passageira
        self.localização_atual = localização_atual
        self.destino = destino
        self.ativo = False
    def __str__(self):
        return f"{self.nome_passageira} | {self.localização_atual} | {self.destino} | {self.ativo}"

pessoa_alisson = Para_onde("alisson", "centro","morumbi")
pessoa_kauane = Para_onde("kauane", "morumbi","vila c")


Para_onde = [pessoa_alisson, pessoa_kauane]
print(pessoa_alisson)
print(pessoa_kauane)





