import matplotlib
import matplotlib.pyplot as plt
import numpy as np
def graficaVelocidadVsTiempo(vo,t,a):
    x = np.linspace(vo, t, 100)
    y=funcVf(vo,a,x)
    print("X: el Dominio ")
    print(x)
    print(" Y: el Rango")
    print(y)
    #Generamos una grafica lineal para una recta en X
    plt.plot(x, y, label='linear')
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title("GRÁFICA VELOCIDAD vs TIEMPO")
    plt.legend()
    plt.savefig('grafica_V_vs_T.png')
    plt.show()
def graficaDistanciaVsTiempo(vo,t,a):
    x = np.linspace(0, t, 100)
    y=funcD(vo,a,x)
    print("X: el Dominio ")
    print(x)
    print(" Y: el Rango")
    print(y)
    #Generamos una grafica lineal para una recta en X
    plt.plot(x, y, label='Cuadratica')
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia')
    plt.title("GRÁFICA VELOCIDAD vs TIEMPO")
    plt.legend()
    plt.savefig('grafica_V_vs_T.png')
    plt.show()
def funcVf(vo,a,tiempo):
 vf=vo+a*tiempo
 return vf
def funcD(vo,a,tiempo):
 d=vo*tiempo+(a/2)*(tiempo*tiempo)
 return d

graficaVelocidadVsTiempo(2,8,2)
#vi, tiempo, aceleracion
#graficaDistanciaVsTiempo(2,8,2)
