class Para_onde:
    nome_passageira = ""
    localização = ""
    destino = ""
    ativo = False

pessoa_alisson = Para_onde()
pessoa_kauane = Para_onde()

pessoa_kauane.nome_passageira = "kauane"
pessoa_kauane.localização= "morumbi"
pessoa_kauane.destino = "centro"
Para_onde = [pessoa_alisson, pessoa_kauane]

print(Para_onde)

