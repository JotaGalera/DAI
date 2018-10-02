#Modulo Burbuja

def Burbuja(array):
    pasa = False


    while pasa == False:
        pasa = True
        for i in range(len(array)-1):
            if(array[i] > array[i+1]):
                pasa = False
                swap = array[i]
                array[i] = array[i+1]
                array[i+1] = swap

    print(array)
