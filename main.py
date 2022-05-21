# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json



class Sucursal(object):
    def __init__(self,sucursal,ejes):
        self.sucursal = sucursal
        self.ejes = ejes


class Eje(object):
    def __init__(self,sucursal, distancia):
        self.sucursal = sucursal
        self.distancia = distancia


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    f = open('map.json')
    data = json.load(f)
    #obj = jsonpickle.decode(data)
    #print("The JSON is: ", obj.sucursal)
    for i in data['mapa']:
        print(i['ejes'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
