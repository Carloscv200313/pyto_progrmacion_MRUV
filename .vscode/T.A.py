import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
global fondo1
ventana_01=tk.Tk()
ventana_01.title("MOVIMIENTO RECTILINEO UNIFORME VARIADO (M.R.U.)")
ventana_01.resizable(0,0)
ventana_01.iconbitmap("imagenes/carrito.ico")
ventana_01.geometry("900x500")
#FONDO DE LA VENTANA PRINCIPAL
fondo1 = ImageTk.PhotoImage(file="imagenes/fondo01.png")
label_fondo = tk.Label( ventana_01, image=fondo1).place(x=0,y=0,relwidth=1,relheight=1)
#funcion para la velocidad inicial 
def V_v_inicial():
    global fondo_vi
    ventana_vi=tk.Toplevel()
    ventana_vi.resizable(0,0)
    ventana_vi.iconbitmap("imagenes/carrito.ico")
    ventana_vi.geometry("900x500")
    ventana_vi.title("VELOCIDAD INICIAL")
    imagen_vi=Image.open("imagenes/fondo_vi.png")
    fondo_vi=ImageTk.PhotoImage(imagen_vi)
    label_fondo_vi=tk.Label(ventana_vi, image=fondo_vi)
    label_fondo_vi.pack()

    V_final= tk.StringVar()
    V_final=tk.Entry(ventana_vi, textvar=V_final, width=10,relief="flat", bg="#38b6ff")
    V_final.place(x=290,y=295)    
    V_final.config(font=("Arial", 14))
    
    tiempo= tk.StringVar()
    tiempo=tk.Entry(ventana_vi, textvariable=tiempo, width=10, relief="flat", bg="#38b6ff")
    tiempo.place(x=290,y=368)    
    tiempo.config(font=("Arial", 14))

    aceleracion= tk.StringVar()
    aceleracion=tk.Entry(ventana_vi, textvariable=aceleracion, width=10, relief="flat", bg="#38b6ff")
    aceleracion.place(x=290,y=438)    
    aceleracion.config(font=("Arial", 14))

    b_calcular = ImageTk.PhotoImage(file="imagenes/icono.png")
    boton_calcular = tk.Button(ventana_vi,image=b_calcular,command=lambda:V_calcular_vi(V_final,tiempo,aceleracion) , cursor="hand2", height=96, width=96)
    boton_calcular.place(x=780,y=380)

    ventana_vi.mainloop()

#funcion para crear la ventana que halla la velocidad final
def V_calcular_vi(V_final,tiempo,aceleracion):
    global fondo_calcular_vi
    vf= float(V_final.get())
    t= float (tiempo.get())
    a= float (aceleracion.get())
    resultado= vf-a*t
    print (resultado)
 
    V_calcular_vi= tk.Toplevel()
    V_calcular_vi.title("CALCULAR ACELERACION")
    V_calcular_vi.geometry("900x500")
    V_calcular_vi.protocol("WM_DELETE_WINDOW", V_calcular_vi.destroy)
    V_calcular_vi.resizable(0,0)

    imagen = Image.open("imagenes/resultado.png")
    fondo_calcular_vi = ImageTk.PhotoImage(imagen)
    # Crear un label con el fondo de imagen
    label = tk.Label(V_calcular_vi, image=fondo_calcular_vi)
    label.pack()
    
    resultado_label=tk.Label(V_calcular_vi, text= resultado, bg="#3676cd")
    resultado_label.place(x=300,y=250)    
    resultado_label.config(font=("Arial",120), fg="white")
    
    V_calcular_vi.mainloop()


def V_v_final():
    global fondo_vf
    ventana_vf=tk.Toplevel()
    ventana_vf.resizable(0,0)
    ventana_vf.iconbitmap("imagenes/carrito.ico")
    ventana_vf.geometry("900x500")
    ventana_vf.title("VELOCIDAD FINAL")
    imagen_vi=Image.open("imagenes/fondo_vf.png")
    fondo_vf=ImageTk.PhotoImage(imagen_vi)
    label_fondo_vf=tk.Label(ventana_vf, image=fondo_vf)
    label_fondo_vf.pack()

    V_inicial= tk.StringVar()
    V_inicial=tk.Entry(ventana_vf, textvar=V_inicial, width=10,relief="flat", bg="#38b6ff")
    V_inicial.place(x=290,y=295)    
    V_inicial.config(font=("Arial", 14))
    
    tiempo= tk.StringVar()
    tiempo=tk.Entry(ventana_vf, textvariable=tiempo, width=10, relief="flat", bg="#38b6ff")
    tiempo.place(x=290,y=368)    
    tiempo.config(font=("Arial", 14))

    distancia= tk.StringVar()
    distancia=tk.Entry(ventana_vf, textvariable=distancia, width=10, relief="flat", bg="#38b6ff")
    distancia.place(x=290,y=438)    
    distancia.config(font=("Arial", 14))

    b_calcular = ImageTk.PhotoImage(file="imagenes/icono.png")
    boton_calcular = tk.Button(ventana_vf,image=b_calcular,command=lambda:V_calcular_vf(V_inicial,tiempo,distancia) , cursor="hand2", height=96, width=96)
    boton_calcular.place(x=780,y=380)

    ventana_vf.mainloop()

#funcion para crear la ventana que halla la velocidad final
def V_calcular_vf(V_inicial,tiempo,distancia):
    global fondo_calcular_vf
    vi= float(V_inicial.get())
    t= float (tiempo.get())
    d= float (distancia.get())
    resultado= float (2*d/t) - vi

 
    v_calcular_vf= tk.Toplevel()
    v_calcular_vf.title("CALCULAR ACELERACION")
    v_calcular_vf.geometry("900x500")
    v_calcular_vf.protocol("WM_DELETE_WINDOW", v_calcular_vf.destroy)
    v_calcular_vf.resizable(0,0)

    imagen = Image.open("imagenes/resultado.png")
    fondo_calcular_vf = ImageTk.PhotoImage(imagen)
    # Crear un label con el fondo de imagen
    label = tk.Label(v_calcular_vf, image=fondo_calcular_vf)
    label.pack()
    
    resultado_label = tk.Label(v_calcular_vf, text=(resultado), bg="#3676cd")
    resultado_label.place(x=300,y=250)    
    resultado_label.config(font=("Arial",120), fg="white")
    
    v_calcular_vf.mainloop()

#funcion para crear la ventana que halla la velocidad final
def V_a():
    global fondo_a
    ventana_a=tk.Toplevel()
    ventana_a.resizable(0,0)
    ventana_a.iconbitmap("imagenes/carrito.ico")
    ventana_a.geometry("900x500")
    ventana_a.title("VELOCIDAD INICIAL")
    imagen_a=Image.open("imagenes/fondo_a.png")
    fondo_a=ImageTk.PhotoImage(imagen_a)
    label_fondo_a=tk.Label(ventana_a, image=fondo_a)
    label_fondo_a.pack()

    V_inicial= tk.StringVar()
    V_inicial=tk.Entry(ventana_a, textvar=V_inicial, width=10,relief="flat", bg="#38b6ff")
    V_inicial.place(x=290,y=295)    
    V_inicial.config(font=("Arial", 14))
    
    tiempo= tk.StringVar()
    tiempo=tk.Entry(ventana_a, textvariable=tiempo, width=10, relief="flat", bg="#38b6ff")
    tiempo.place(x=290,y=368)    
    tiempo.config(font=("Arial", 14))

    distancia= tk.StringVar()
    distancia=tk.Entry(ventana_a, textvariable=distancia, width=10, relief="flat", bg="#38b6ff")
    distancia.place(x=290,y=438)    
    distancia.config(font=("Arial", 14))

    b_calcular = ImageTk.PhotoImage(file="imagenes/icono.png")
    boton_calcular = tk.Button(ventana_a,image=b_calcular,command=lambda:V_calcular_a(V_inicial,tiempo,distancia) , cursor="hand2", height=96, width=96)
    boton_calcular.place(x=780,y=380)

    ventana_a.mainloop()

#funcion para crear la ventana que halla la velocidad inicial
def V_calcular_a(V_inicial,tiempo,distancia):
    global fondo_calcular_a
    vi= float(V_inicial.get())
    t= float (tiempo.get())
    d= float (distancia.get())
    resultado= (2*(d - vi*t))/pow(t,2)
    print (resultado)
 
    V_calcular_a= tk.Toplevel()
    V_calcular_a.title("CALCULAR ACELERACION")
    V_calcular_a.geometry("900x500")
    V_calcular_a.protocol("WM_DELETE_WINDOW", V_calcular_a.destroy)
    V_calcular_a.resizable(0,0)

    imagen = Image.open("imagenes/resultado.png")
    fondo_calcular_vi = ImageTk.PhotoImage(imagen)
    # Crear un label con el fondo de imagen
    label = tk.Label(V_calcular_a, image=fondo_calcular_vi)
    label.pack()
    
    resultado_label=tk.Label(V_calcular_a, text= resultado, bg="#3676cd")
    resultado_label.place(x=300,y=250)    
    resultado_label.config(font=("Arial",120), fg="white")
    
    V_calcular_a.mainloop()

#funcion para la distancia 
def V_d():
    global fondo_d
    ventana_d=tk.Toplevel()
    ventana_d.resizable(0,0)
    ventana_d.iconbitmap("imagenes/carrito.ico")
    ventana_d.geometry("900x500")
    ventana_d.title("VELOCIDAD INICIAL")
    imagen_d=Image.open("imagenes/fondo_d.png")
    fondo_d=ImageTk.PhotoImage(imagen_d)
    label_fondo_d=tk.Label(ventana_d, image=fondo_d)
    label_fondo_d.pack()

    V_inicial= tk.StringVar()
    V_inicial=tk.Entry(ventana_d, textvar=V_inicial, width=10,relief="flat", bg="#38b6ff")
    V_inicial.place(x=290,y=295)    
    V_inicial.config(font=("Arial", 14))
    
    aceleracion= tk.StringVar()
    aceleracion=tk.Entry(ventana_d, textvariable=aceleracion, width=10, relief="flat", bg="#38b6ff")
    aceleracion.place(x=290,y=368)    
    aceleracion.config(font=("Arial", 14))

    tiempo= tk.StringVar()
    tiempo=tk.Entry(ventana_d, textvariable=tiempo, width=10, relief="flat", bg="#38b6ff")
    tiempo.place(x=290,y=438)    
    tiempo.config(font=("Arial", 14))


    b_calcular = ImageTk.PhotoImage(file="imagenes/icono.png")
    boton_calcular = tk.Button(ventana_d,image=b_calcular,command=lambda:V_calcular_d(V_inicial,aceleracion,tiempo) , cursor="hand2", height=96, width=96)
    boton_calcular.place(x=780,y=380)

    ventana_d.mainloop()

#funcion para crear la ventana que halla la distancia
def V_calcular_d(V_inicial,aceleracion,tiempo):
    global fondo_calcular_d
    vi= float(V_inicial.get())
    t= float (tiempo.get())
    a= float (aceleracion.get())
    resultado= vi*t + (a*pow(t,2))/2
    print (resultado)
 
    V_calcular_d= tk.Toplevel()
    V_calcular_d.title("CALCULAR ACELERACION")
    V_calcular_d.geometry("900x500")
    V_calcular_d.protocol("WM_DELETE_WINDOW", V_calcular_d.destroy)
    V_calcular_d.resizable(0,0)

    imagen = Image.open("imagenes/resultado.png")
    fondo_calcular_d = ImageTk.PhotoImage(imagen)
    # Crear un label con el fondo de imagen
    label = tk.Label(V_calcular_d, image=fondo_calcular_d)
    label.pack()
    
    resultado_label=tk.Label(V_calcular_d, text= resultado, bg="#3676cd")
    resultado_label.place(x=300,y=250)    
    resultado_label.config(font=("Arial",120), fg="white")
    
    V_calcular_d.mainloop()

#funcion para la distancia 
def V_t():
    global fondo_t
    ventana_t=tk.Toplevel()
    ventana_t.resizable(0,0)
    ventana_t.iconbitmap("imagenes/carrito.ico")
    ventana_t.geometry("900x500")
    ventana_t.title("VELOCIDAD INICIAL")
    imagen_d=Image.open("imagenes/fondo_t.png")
    fondo_d=ImageTk.PhotoImage(imagen_d)
    label_fondo_d=tk.Label(ventana_t, image=fondo_d)
    label_fondo_d.pack()

    V_inicial= tk.StringVar()
    V_inicial=tk.Entry(ventana_t, textvar=V_inicial, width=10,relief="flat", bg="#38b6ff")
    V_inicial.place(x=290,y=295)    
    V_inicial.config(font=("Arial", 14))
    
    v_final= tk.StringVar()
    v_final=tk.Entry(ventana_t, textvariable=v_final, width=10, relief="flat", bg="#38b6ff")
    v_final.place(x=290,y=368)    
    v_final.config(font=("Arial", 14))

    distancia= tk.StringVar()
    distancia=tk.Entry(ventana_t, textvariable=distancia, width=10, relief="flat", bg="#38b6ff")
    distancia.place(x=290,y=438)    
    distancia.config(font=("Arial", 14))


    b_calcular = ImageTk.PhotoImage(file="imagenes/icono.png")
    boton_calcular = tk.Button(ventana_t,image=b_calcular,command=lambda:V_calcular_t(V_inicial,v_final,distancia) , cursor="hand2", height=96, width=96)
    boton_calcular.place(x=780,y=380)

    ventana_t.mainloop()

#funcion para crear la ventana que halla tiempo
def V_calcular_t(V_inicial,v_final,distancia):
    global fondo_calcular_d
    vi= float(V_inicial.get())
    vf= float (v_final.get())
    d= float (distancia.get())
    resultado= 2*d/(vi+vf)
    print (resultado)
 
    V_calcular_d= tk.Toplevel()
    V_calcular_d.title("CALCULAR ACELERACION")
    V_calcular_d.geometry("900x500")
    V_calcular_d.protocol("WM_DELETE_WINDOW", V_calcular_d.destroy)
    V_calcular_d.resizable(0,0)

    imagen = Image.open("imagenes/resultado.png")
    fondo_calcular_d = ImageTk.PhotoImage(imagen)
    # Crear un label con el fondo de imagen
    label = tk.Label(V_calcular_d, image=fondo_calcular_d)
    label.pack()
    
    resultado_label=tk.Label(V_calcular_d, text= resultado, bg="#3676cd")
    resultado_label.place(x=300,y=250)    
    resultado_label.config(font=("Arial",120), fg="white")
    
    V_calcular_d.mainloop()

def V_gvt ():
    global fondo_d
    ventana_d=tk.Toplevel()
    ventana_d.resizable(0,0)
    ventana_d.iconbitmap("imagenes/carrito.ico")
    ventana_d.geometry("900x500")
    ventana_d.title("GRAFICA: VELOCIDAD INICIAL vs. TIEMPO")
    imagen_d=Image.open("imagenes/fondo_gvt.png")
    fondo_d=ImageTk.PhotoImage(imagen_d)
    label_fondo_d=tk.Label(ventana_d, image=fondo_d)
    label_fondo_d.pack()

    V_inicial= tk.StringVar()
    V_inicial=tk.Entry(ventana_d, textvar=V_inicial, width=10,relief="flat", bg="#38b6ff")
    V_inicial.place(x=290,y=295)    
    V_inicial.config(font=("Arial", 14))
    
    tiempo= tk.StringVar()
    tiempo=tk.Entry(ventana_d, textvariable=tiempo, width=10, relief="flat", bg="#38b6ff")
    tiempo.place(x=290,y=368)    
    tiempo.config(font=("Arial", 14))


    aceleracion= tk.StringVar()
    aceleracion=tk.Entry(ventana_d, textvariable=aceleracion, width=10, relief="flat", bg="#38b6ff")
    aceleracion.place(x=290,y=438)    
    aceleracion.config(font=("Arial", 14))




    b_calcular = ImageTk.PhotoImage(file="imagenes/icono_grafica.png")
    boton_calcular = tk.Button(ventana_d,image=b_calcular,command=lambda:V_graficar_vt(V_inicial,tiempo, aceleracion) , cursor="hand2", height=96, width=96)
    boton_calcular.place(x=780,y=380)

    ventana_d.mainloop()

def graficaVelocidadVsTiempo(vo,t,a):
    x = np.linspace(0, t, 100)
    y=funcVf(vo,a,x)
    print("X: el Dominio ")
    print(x)
    print(" Y: el Rango")
    print(y)
    #Generamos una grafica lineal para una recta en X
    #ax=plt.subplot();
    plt.plot(x, y, label='linear', color="blue")
   # Mostrar solo 10 valores en el eje X y 10 valores en el eje Y
    x_ticks = np.linspace(min(x), max(x), 10)
    y_ticks = np.linspace(min(y), max(y), 10)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.fill_between(x,y,color='#87CEEB',alpha=0.5)
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad')
    plt.title("GRÁFICA VELOCIDAD vs TIEMPO")
    plt.legend()
    plt.savefig('grafica_V_vs_T.png')
    plt.show()
    
def funcVf(vo,a,tiempo):
    vf=vo+a*tiempo
    return vf

#funcion para crear la ventana que halla la distancia
def V_graficar_vt(V_inicial,tiempo, aceleracion):
    vi= float(V_inicial.get())
    t= float (tiempo.get())
    a= float (aceleracion.get())
    graficaVelocidadVsTiempo(vi,t,a)

def V_gdt():
    global fondo_d
    ventana_d=tk.Toplevel()
    ventana_d.resizable(0,0)
    ventana_d.iconbitmap("imagenes/carrito.ico")
    ventana_d.geometry("900x500")
    ventana_d.title("GRAFICA: VELOCIDAD INICIAL vs. TIEMPO")
    imagen_d=Image.open("imagenes/fondo_gdt.png")
    fondo_d=ImageTk.PhotoImage(imagen_d)
    label_fondo_d=tk.Label(ventana_d, image=fondo_d)
    label_fondo_d.pack()

    V_inicial= tk.StringVar()
    V_inicial=tk.Entry(ventana_d, textvar=V_inicial, width=10,relief="flat", bg="#38b6ff")
    V_inicial.place(x=290,y=295)    
    V_inicial.config(font=("Arial", 14))
    
    tiempo= tk.StringVar()
    tiempo=tk.Entry(ventana_d, textvariable=tiempo, width=10, relief="flat", bg="#38b6ff")
    tiempo.place(x=290,y=368)    
    tiempo.config(font=("Arial", 14))


    aceleracion= tk.StringVar()
    aceleracion=tk.Entry(ventana_d, textvariable=aceleracion, width=10, relief="flat", bg="#38b6ff")
    aceleracion.place(x=290,y=438)    
    aceleracion.config(font=("Arial", 14))




    b_calcular = ImageTk.PhotoImage(file="imagenes/icono_grafica.png")
    boton_calcular = tk.Button(ventana_d,image=b_calcular,command=lambda:V_graficar_dt(V_inicial,tiempo, aceleracion) , cursor="hand2", height=96, width=96)
    boton_calcular.place(x=780,y=380)

    ventana_d.mainloop()

def graficaDistanciaVsTiempo(vo,t,a):
    x = np.linspace(0, t, 100)
    y=funcD(vo,a,x)
    print("X: el Dominio ")
    print(x)
    print(" Y: el Rango")
    print(y)
    #Generamos una grafica cuadratica para una recta en X
    plt.plot(x, y, label='Cudratica', color="green")
   # Mostrar solo 10 valores en el eje X y 10 valores en el eje Y
    x_ticks = np.linspace(min(x), max(x), 10)
    y_ticks = np.linspace(min(y), max(y), 10)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.fill_between(x,y,color='green',alpha=0.3)
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia')
    plt.title("GRÁFICA VELOCIDAD vs TIEMPO")
    plt.legend()
    plt.savefig('grafica_V_vs_T.png')
    plt.show()

def funcD(vo,a,tiempo):
    d=vo*tiempo+(a/2)*(tiempo*tiempo)
    return d

def V_graficar_dt(V_inicial,tiempo, aceleracion):
    vi= float(V_inicial.get())
    t= float (tiempo.get())
    a= float (aceleracion.get())
    graficaDistanciaVsTiempo(vi,t,a)



#botones 
b_vi = ImageTk.PhotoImage(file="imagenes/boton_vi.gif")
boton_vi=tk.Button(ventana_01, image=b_vi,command=V_v_inicial, height=70, width=200).place(x=400,y=20)

b_vf = ImageTk.PhotoImage(file="imagenes/boton_vf.gif")
boton_vf=tk.Button(ventana_01, image=b_vf,command=V_v_final, height=70, width=200).place(x=400,y=110)

b_a = ImageTk.PhotoImage(file="imagenes/boton_a.gif")
boton_a=tk.Button(ventana_01, image=b_a, height=70,command=V_a, width=200).place(x=400,y=200)


b_d = ImageTk.PhotoImage(file="imagenes/boton_d.gif")
boton_d=tk.Button(ventana_01, image=b_d, height=70,command=V_d, width=200).place(x=400,y=290)


b_t = ImageTk.PhotoImage(file="imagenes/boton_t.gif")
boton_t=tk.Button(ventana_01, image=b_t, height=70,command=V_t, width=200).place(x=400,y=380)


b_g_DxT = ImageTk.PhotoImage(file="imagenes/g_DxT.gif")
boton_g_DxT=tk.Button(ventana_01, image=b_g_DxT, height=100 ,command=V_gdt, width=200).place(x=650,y=30)


b_g_VxT = ImageTk.PhotoImage(file="imagenes/g_VxT.gif")
boton_g_VxT=tk.Button(ventana_01, image=b_g_VxT, height=100,command=V_gvt, width=200).place(x=650,y=180)

b_s = ImageTk.PhotoImage(file="imagenes/SIMULACION.png")
boton_s=tk.Button(ventana_01, image=b_s, height=100, width=200).place(x=650,y=330)


ventana_01.mainloop()