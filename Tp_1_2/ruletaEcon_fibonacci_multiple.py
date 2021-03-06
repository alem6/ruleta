import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
import math
from tkinter import *

def getNthFib(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n > 2:
		return getNthFib(n-1) + getNthFib(n-2)

def getColor(numero):
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10 , 11 , 13 , 15 , 17 ,20 , 22 , 24 ,26, 28, 29 , 31 , 33 , 35]
    if numero == 0: 
        return "V"
    if numero in rojos:
        return "R"
    else:
        return "N"

def getParidad(numero):
    if (numero % 2 == 0): 
        return "P" 
    else:
        return "I"

def opcionMenu():
    for i in opciones.pack_slaves():
            i.destroy() 
    if opcion.get() == 1: # Numero
        #Limpia        
        Label(opciones , text = "Ingrese el numero al que desea apostar").pack()
        Entry(opciones , textvariable = num ).pack()

        Button(opciones , command = apostar , text = "Apostar").pack()

    elif opcion.get() == 2: # Color
        #Limpia
        Label(opciones , text = "Ingrese el color al que desea apostar (R ,N)").pack()
        Entry(opciones , textvariable = col).pack()

        Button(opciones , command = apostar , text = "Apostar").pack()


    elif opcion.get() == 3: # Paridad
        #Limpia
        Label(opciones , text = "Ingrese si desea apostar a par o impar (I , P)").pack()
        Entry(opciones , textvariable = par).pack()


        Button(opciones , command = apostar, text = "Apostar").pack()
        
def getMax(array):
    """
        Max in an array of integer arrays
    """
    maximum = 0
    for arr in array:
        if max(arr) > maximum: 
            maximum = max(arr)
    return maximum
def getGano(modo, numero_random , apuesta , color_apostado , numero_apostado , paridad_apostado):
    gano = 0

    if modo == 1: # Numero
        if numero_apostado == numero_random:
            gano = apuesta * 36     
    elif modo == 2: #Color
        if color_apostado == getColor(numero_random):
            gano = apuesta * 2
    elif modo == 3: #Par/Impar
        if paridad_apostado == getParidad(numero_random):
            gano = apuesta * 2
    
    return gano

def apostar(): 
    cantVeces = 1000
    cantJugadas = 5
    modo = opcion.get()  # 1 2 3
    
    infinito = True
    debug = False
 # Busca los parametros de la apuesta que puede   

    try:
        numero = int(num.get())
    except:
        numero = 0
    try:
        color = str(col.get())
    except:
        color = ""
    try:
        paridad = str(par.get())
    except:
        paridad = ""
    
    n = 1
    plata = 10000
    plata_inicial = plata
    apuesta = getNthFib(n)
    altura = plata
    cant_capital = [[],[],[],[],[]]
    frec_relativas = [[],[],[],[],[]]
    dinero_ganado = [[],[],[],[],[]] 
    c  = 0   
    for x in range(0, cantJugadas):
        plata = 10000
        cant_ganadas = 0
        n = 1
        for i in range(1 , cantVeces + 1):
            nroaleatorio = random.randrange( 00, 37)
            apuesta = getNthFib(n)
            if not infinito:
                if apuesta > plata: 
                    print(F"-------------- HAS PERDIDO (Corrida {x + 1})----------------------" )
                    break
            gano = getGano(modo , nroaleatorio , apuesta , color , numero , paridad)
            if gano > 0 :
                dinero_ganado[x].append(gano)
            else:
                dinero_ganado[x].append(-apuesta)
            if gano == 0:
                n += 1
                plata -= apuesta
                c += 1
            if gano > 0:
                plata -= apuesta
                plata += gano
                cant_ganadas += 1


                c+=1
                if n > 3:
                    n -= 2
                else:
                    n = 1
            frec_relativas[x].append(cant_ganadas / i)
            cant_capital[x].append(plata)
            if debug : print(f"Aposto {apuesta} y tiene {plata}")


    colores = ["r", "b", "g" , "c" , "m"]
    for index , arrayFrecuencia in enumerate(frec_relativas):
        x_coords = np.arange(len(arrayFrecuencia)) 
        plt.bar(x_coords + index / 10, arrayFrecuencia , width = 0.1 , color = colores[index]  , label = f"FR corrida {index + 1}")
    plt.xlabel("N")
    plt.ylabel("FR")
    plt.legend()
    plt.show()
    #plt.savefig("fib_fr_li.png")
    #plt.clf()
    
    
    for index , cant_c in enumerate(cant_capital):
        plt.plot(cant_c , color = colores[index] , label = f"Flujo de caja corrida {index + 1}" )
    plt.axhline(y = plata_inicial, color = "y", label = "Dinero inicial")
    plt.xlabel("N")
    plt.ylabel("Cant Capital")
    plt.legend()
    #plt.savefig("fib_cc_li.png")
    #plt.clf()
    plt.show()

    max_dinero = getMax(cant_capital)
    
    for index, cant_c in enumerate(cant_capital) :
        x_coords = np.arange(len(cant_c)) 
        plt.bar(x_coords + index / 10, cant_c , width = 0.1 , color = colores[index]  , label = f"Flujo de caja corrida {index + 1}")
    plt.axhline(y = max_dinero, color = "y", label = "Dinero maximo")
    plt.xlabel("N")
    plt.ylabel("Cant Capital")
    plt.legend()
    #plt.savefig("fib_ccb_li.png")
    #plt.clf()
    
    plt.show()
    for index, gain in enumerate(dinero_ganado):
        plt.plot(gain , color = colores[index] , label = f"Ganancia-Perdida/Tiro {index + 1}" )
    plt.xlabel("N")
    plt.ylabel("Ganancia")
    plt.legend()
    #plt.savefig("fib_gpt_li.png")
    #plt.clf()
    plt.show()
    #region Graphs
    #    
    #  
    ##Grafica de Capital
    #
    #plt.axhline(altura)
    #plt.ylabel("CC(Cantidad de Capital)")
    #plt.xlabel("Numero de tiradas")
    #plt.axis([ 0 , len(cant_capital) - 1 , 0 , max(cant_capital) + 10])
    #plt.plot(cant_capital, "-r")
    ##plt.show()
    #plt.savefig("cc.png")
    #plt.clf()
    ##grafica barras
    #
    #datos1=[cant_capital]
    #X=np.arange(len(cant_capital)) 
    #plt.bar(X,datos1[0],color='g',width=0.25)
    #plt.axhline(plata , lw = 8)
    #plt.ylabel("CC(Cantidad de Capital)")
    #plt.xlabel("Numero de tiradas")
    #plt.axis([ 0 , len(cant_capital), 0 , max(cant_capital) + 10])
    ##plt.show()
    #plt.tight_layout()
    #plt.savefig("barrascc.png")
    #plt.clf()
    ##Frec Relativa
    #x_coords = np.arange(len(frec_relativas))
    #plt.bar(x_coords , frec_relativas , width = 0.25 , color = "b")
    #plt.ylabel("Frecuencias Relativas")
    #plt.xlabel("Numero de tiradas")
    ##plt.show()
    #plt.savefig("fr.png")
    #plt.clf()
    ##Ganancia por tiro
    #width = 0.3
    #x_coords = np.arange(len(dinero_ganado))
    #plt.bar(x_coords + width / 2, dinero_ganado, width = width , color = "g", label = "Dinero Ganado")
    #plt.ylabel("Frecuencias Relativas")
    #plt.xlabel("Numero de tiradas")
    #plt.axis([ 0 ,len(dinero_ganado) - 1, 0 , max(dinero_ganado) + 10])
    #plt.legend()
    ##plt.show()
    #plt.savefig("gpt.png")   
    #plt.clf()  
    #endregion
#region Menu
#Menu
root = Tk()
root.title("Ruleta")

opcion  = IntVar()
num  = StringVar()
apue = StringVar()
col   = StringVar()
par = StringVar()


# Labels
frame = Frame(root, width = 600 , height = 600)
frame.pack()
label = Label(frame, text = "Bienvenido a la ruleta")
label.config(font = ("Verdana", 20))
label.grid(row = 0 , column = 1, pady = 20)
label = Label(frame, text = "Elija a que desea apostar")
label.config(font = ("Verdana", 16))
label.grid(row = 1 , column = 1 , pady = 5 , padx = 20)

Radiobutton(frame , text = "Numero     "    ,variable = opcion , value = 1, command = opcionMenu).grid(row = 2 ,column = 1)
Radiobutton(frame , text = "Color\t"        ,variable = opcion , value = 2, command = opcionMenu).grid(row = 3 ,column = 1)
Radiobutton(frame , text = "Par / Impar"    ,variable = opcion , value = 3, command = opcionMenu).grid(row = 4 ,column = 1)

opciones = Frame(root)
opciones.pack()

#Loop principal
root.mainloop()

#endregion
