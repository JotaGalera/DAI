#Modulo Seleccion.py

def Seleccion(array):
    for fillslot in range(len(array)-1,0,-1):
        pmax = 0
        for location in range(1,fillslot+1):
            if array[location] > array[pmax]:
                pmax = location
        array[fillslot],array[pmax] = array[pmax],array[fillslot]

    print(array)
