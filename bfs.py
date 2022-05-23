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


visited = []


total_expl = 0
total_desc = 0


def bfs_new(inicio, destino, costo):
    visitado = {}
    nivel = {}
    padre = {}
    salida = []
    check_dest = []
    cola = Queue()

    for nodo in grafo.keys():
        visitado[nodo] = False
        padre[nodo] = None
        nivel[nodo] = -1

    s = inicio
    visitado[s] = True
    nivel[s] = 0
    cola.put(s)

    while not cola.empty():
        u = cola.get()
        salida.append(u)
        # print("La sucursal", u, "tiene aristas con: ")
        for v in grafo[u]:
            if not visitado[v]:
                visitado[v] = True
                padre[v] = u
                nivel[v] = nivel[u] + 1
                cola.put(v)
    global total_desc
    total_desc += len(salida)
    # print(salida)

    v = destino
    camino = []
    while v is not None:
        camino.append(v)
        v = padre[v]
    camino.reverse()
    return camino


def bfs_full(inicio, destinos, costo):
    fromhere = inicio
    valores = []
    conteo = 0
    destinos.append(inicio)
    for d in destinos:
        if d == inicio:
            store = bfs_new(fromhere, d, costo)
            if conteo > 0:
                store.pop(0)
                valores.extend(store)
            else:
                valores.extend(store)
            fromhere = d
        elif d not in valores:
            store = bfs_new(fromhere, d, costo)
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
    bfs_full(origen,destinos,costo_max)
    print("Tiempo transcurrido:", (time.time() - tiempo_inicio))
    print("Total de Nodos descubiertos:", total_desc)
    print("Total de Nodos explorados:", total_expl)

    """costo_uniforme_full(origen, destinos, costo_max)
    print("Tiempo transcurrido:", (time.time() - tiempo_inicio))
    print("Total de Nodos descubiertos:", total_desc)
    print("Total de Nodos explorados:", total_expl)"""
    """print("Following is the Breadth-First Search")
    bfs(visited, graph, '5', '2')  # function calling
    print("Regresando...")
    bfs(visited, graph, '2', '5')"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
