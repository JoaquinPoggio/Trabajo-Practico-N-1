def usar_la_fuerza(mochila, objetos =0):
    if not mochila:
        print("No se encontro el sable de luz.")
        return False, objetos
    
    if mochila[0] == 'sable de luz':
        print("Si se encontro un sable de luz")
        return True, objetos+1
    else:
        print(f"Se saco el objeto '{mochila[0]}' de la mochila")
        return usar_la_fuerza(mochila[1:], objetos + 1)

def ingresar_mochila(mochila=None):
    if mochila is None:
        mochila = []
    
    objeto = input("Ingrese un objeto para la mochila (o 'fin' para terminar): ")
    if objeto != 'fin':
        mochila = mochila + [objeto]
        return ingresar_mochila(mochila)
    else:
        return mochila


mochila=ingresar_mochila()
encontrado, objetos_necesarios = usar_la_fuerza(mochila)
if encontrado:  
    print(f"Se necesitaron sacar {objetos_necesarios} objetos para encontrar el sable de luz en la mochila")