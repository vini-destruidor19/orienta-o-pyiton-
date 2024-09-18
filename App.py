from modelo.para_onde import Para_onde

pessoa_Alisson = Para_onde("Alisson", "centro","morumbi")
pessoa_kauane = Para_onde("kauane", "Morumbi","vila c")
pessoa_Samuel = Para_onde("Samuel", "Portal", "UDC centro" )
pessoa_Gustavo = Para_onde("Gustavo", "Panorama Morumbi", "Panorama JK")

pessoa_Alisson.altenativa_destino()
pessoa_Samuel.receber_Preco("Rota 1", 15)
pessoa_Samuel.receber_Preco('Rota 2', 30)

pessoa_kauane.receber_Preco("Rota 1", 20)
pessoa_kauane.receber_Preco('Rota 2', 32)

pessoa_Gustavo.receber_Preco("Rota 1", 15)
pessoa_Gustavo.receber_Preco('Rota 2', 25)

def main():
    Para_onde.listar_destino()

if __name__== "__main__":
    main()
