# GuardedUSB
# Emmanuel Bandres, 14-10071
# Daniela Caballero, 14-10140

import sys, Parser, Eval

if __name__ == '__main__':
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

    ast = Parser.parsear(content)
    #test = str(ast)
    #while "\n\n" in test: test = test.replace("\n\n", "\n")
    #print(test)
    try:
        Eval.eval_ast(ast)
    except IndexError as e:
        print("Error: index out of bounds in line", e)
        sys.exit(1)
    except ZeroDivisionError as e:
        print("Error: Zero division in line", e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
