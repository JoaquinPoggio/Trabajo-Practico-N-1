def usar_la_fuerza(mochila, posicion=0, objetos=0):
    if len(mochila) == 0:
        print("No se encontro el sable de luz")
        return False, objetos
    
    if 'sable de luz' in mochila:
        print("Si se encontro un sable de luz")
        return True, objetos + mochila.index('sable de luz') + 1
    else:
        print(f"Se saco el objeto '{mochila[posicion]}' de la mochila")
        return usar_la_fuerza(mochila, posicion + 1, objetos + 1)

mochila = []
while True:
    objeto = input("Ingrese un objeto de la mochila (o fin para terminar): ")
    if objeto.lower() == 'fin':
        break
    mochila.append(objeto)

encontrado, objetos_necesarios = usar_la_fuerza(mochila.copy())
if encontrado:  
    print(f"Se necesitaron sacar {objetos_necesarios} objetos para encontrar el sable de luz en la mochila")