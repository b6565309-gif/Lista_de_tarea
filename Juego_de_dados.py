import random 

def dado_6_caras():
	numero = random.randint(1,6)
	print(f"salio {numero} en el dado")
	
def dado_12_caras():
	numero = random.randint(1,12)
	print(f"salio el numero {numero} en el dado de 12 caras")
	
def dado_24_caras():
	numero = random.randint(1,24)
	print(f"en el dado de 24 caras salio ... el numero {numero}!")
	
def menu():
	print("\n🎲juego de dados,elije cual vas a tirar🎲")
	print("1. dado de 6 caras")
	print("2. dado de 12 caras")
	print("3. dado de 24 caras")
	print("4. salir")
 
	
def main():
	while True:
		menu()
		opcion = input("elije una opcion: ")
		if opcion == "1":
			dado_6_caras()
		elif opcion == "2":
			dado_12_caras()
		elif opcion == "3":
			dado_24_caras()
		elif opcion == "4":
			print("adios!!")
			break
		else:
			print("elije una opcion valida")
			
if __name__ == "__main__":
	main()
	
