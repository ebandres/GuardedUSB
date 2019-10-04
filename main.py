# Emmanuel Bandres, 14-10071
# Daniela Caballero, 14-10140

import Lexer, sys

def main():
	# Revisamos que el archivo se indique en el comando y que sea .gusb
	if len(sys.argv) != 2:
		print("Error: Indicar el nombre del archivo a leer")
		exit(1)
	elif sys.argv[1][len(sys.argv[1]) - 5:] != ".gusb":
		print("Error: El archivo indicado no es un archivo de GuardedUSB")
		exit(1)
	
	# Leemos el contenido del archivo
	content = ""
	with open(sys.argv[1], 'r') as file:
		content = file.read()

	# Enviamos el contenido del archivo al Lexer
	Lexer.tokenize(content)

if __name__ == "__main__":
	main()