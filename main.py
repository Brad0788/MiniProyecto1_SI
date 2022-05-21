# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json


#Estas clases las cree por una librería que queria probar pero no sirvió, las dejé ahí talvez nos sirvan de algo
class Sucursal(object):
    def __init__(self,sucursal,ejes):
        self.sucursal = sucursal
        self.ejes = ejes

#Estas clases las cree por una librería que queria probar pero no sirvió, las dejé ahí talvez si nos sirvan de algo
class Eje(object):
    def __init__(self,sucursal, distancia):
        self.sucursal = sucursal
        self.distancia = distancia


def print_mapa():
    f = open('map.json')
    data = json.load(f)
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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_mapa()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
