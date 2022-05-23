# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import queue
import time
from queue import Queue, PriorityQueue
import sys

# Estas clases las cree por una librería que queria probar pero no sirvió, las dejé ahí talvez nos sirvan de algo
class Sucursal(object):
    def __init__(self,sucursal,ejes):
        self.sucursal = sucursal
        self.ejes = ejes


# Estas clases las cree por una librería que queria probar pero no sirvió, las dejé ahí talvez si nos sirvan de algo
class Eje(object):
    def __init__(self,sucursal, distancia):
        self.sucursal = sucursal
        self.distancia = distancia


sucursales = []
dict_distancias = {}

grafo = {}


def costo_uniforme(inicio, destino):
    visitado = []
    frontera = PriorityQueue()
    frontera.put((0, inicio))
    global total_desc

    camino = []
    padre = {}
    camino2 = []
    explorado = []

    for nodo in grafo.keys():
        padre[nodo] = None

    while True:
        get_front = frontera.get()
        total_desc += 1
        print(get_front)
        val = 0
        peso, actual = get_front
        if actual not in explorado:
            explorado.append(actual)

        if actual == destino:
            vec = destino
            while vec is not None:
                camino2.append(vec)
                vec = padre[vec]
            camino2.reverse()
            print("El camino sería:")
            print(camino2)
            # for nodo in camino:
                # print("Sucursal:", nodo[0], "Costo:", nodo[1])
            return camino2
        for nodo in grafo[actual]:
            if nodo not in explorado:
                val = peso + dict_distancias[actual, nodo]
                frontera.put((val, nodo))
                padre[nodo] = actual
        if actual not in camino:
            camino.append([actual, val])


visited = []


total_expl = 0
total_desc = 0


def costo_uniforme_full(inicio, destinos, costo):
    fromhere = inicio
    valores = []
    conteo = 0
    destinos.append(inicio)
    for d in destinos:
        if d == inicio:
            store = costo_uniforme(fromhere, d)
            if conteo > 0:
                store.pop(0)
                valores.extend(store)
            else:
                valores.extend(store)
            fromhere = d
        elif d not in valores:
            store = costo_uniforme(fromhere, d)
            if conteo > 0:
                store.pop(0)
                valores.extend(store)
            else:
                valores.extend(store)
            fromhere = d
        conteo += 1
    sum = 0
    count = 0
    while count < len(valores)-2:
        sum += dict_distancias[valores[count], valores[count+1]]
        count += 1
    if sum > costo_max:
        print("El costo es muy alto, ha fallado la busqueda")
    else:
        print("El camino mas corto sería: ")
        print(valores)
    global total_expl
    total_expl = len(valores)


def print_mapa():
    f = open(sys.argv[1])
    data = json.load(f)
    file = open(sys.argv[2])
    print(file)
    # obj = jsonpickle.decode(data)
    # print("The JSON is: ", obj.sucursal)
    j = 1
    for i in data['mapa']:
        ejes = i['ejes']
        print("La sucursal", i['sucursal'], "tiene como vecinos a: ")
        for eje in ejes:
            print(eje['sucursal'], "a una distancia de", eje['distancia'])
        print()
        # print(j, " ", i['ejes'])
        j += 1


def create_graph():
    f = open(sys.argv[1])
    data = json.load(f)
    edges = []
    for i in data['mapa']:
        sucursales.append(i['sucursal'])
        ejes = i['ejes']
        lista = []
        for eje in ejes:
            dict_distancias[(i['sucursal'], eje['sucursal'])] = eje['distancia']
            lista.append(eje['sucursal'])
        grafo[i['sucursal']] = lista
    # print(grafo)
    # print(dict_distancias)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_mapa()
    tiempo_inicio = time.time()
    file = open(sys.argv[2])
    origen = ""
    costo_max = 0
    conteo = 0
    destinos = []
    for line in file:
        if conteo == 0:
            origen = line.strip()
        elif conteo == 1:
            costo_max = float(line.strip())
        else:
            destinos.append(line.strip())
        # print(line, end="\0")
        conteo += 1
    # print()
    file.close()
    create_graph()
    """bfs_full(origen,destinos,costo_max)
    print("Tiempo transcurrido:", (time.time() - tiempo_inicio))
    print("Total de Nodos descubiertos:", total_desc)
    print("Total de Nodos explorados:", total_expl)"""

    costo_uniforme_full(origen, destinos, costo_max)
    print("Tiempo transcurrido:", (time.time() - tiempo_inicio))
    print("Total de Nodos descubiertos:", total_desc)
    print("Total de Nodos explorados:", total_expl)
    """print("Following is the Breadth-First Search")
    bfs(visited, graph, '5', '2')  # function calling
    print("Regresando...")
    bfs(visited, graph, '2', '5')"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
