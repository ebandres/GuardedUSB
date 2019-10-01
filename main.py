import Lexer, sys

def main():
	if len(sys.argv) != 2:
		print("Error: Indicar el nombre del archivo a leer")
		exit(1)
	elif sys.argv[1][len(sys.argv[1]) - 5:] != ".gusb":
		print("Error: El archivo indicado no es un archivo de GuardedUSB")
		exit(1)
	
	content = ""

	with open('archivo.gusb', 'r') as file:
		content = file.read()

if __name__ == "__main__":
	main()