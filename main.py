#IMPORTS DE LIBRERIAS NECESARIAS main class
from cProfile import label
from textwrap import fill, wrap
import tkinter
from tkinter.ttk import Label
from tkinter import *
from tokenize import String
from PIL import ImageTk,Image

#IMPORTS de librerias para class Operaciones
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from cmath import cos
from scipy.integrate import quad
# Pi es una constante definida en numpy
from numpy import pi
import numpy as np
# Para ignorar Tos warnings
import warnings
warnings.filterwarnings("ignore")
#IMPORTS DE LIBRERIAS NECESARIAS


#############################################
#############################################
####DECLARACION METODOS DE SERIES

def buildFunction(array_f,array_iniciales,array_finales,t):
    resultado=0
    print("")
    print("t:"+str(t))
    print("valor:"+str(array_f[1].get()))
    print("incial:"+str(array_iniciales[1].get()))
    print("final:"+str(array_finales[1].get()))
    if (t>array_iniciales[0].get()) and (t<array_finales[0].get()):
        print("entramos en 1")
        resultado=array_f[0].get()
    elif (t>array_iniciales[1].get()) and (t<array_finales[1].get()):
        print("entramos en 2")
        resultado=array_f[1].get()
    elif (t>array_iniciales[2].get()) and (t<array_finales[2].get()):
        print("entramos en 3")
        resultado=array_f[2].get()
    print("valor obtenido por y: " + str(resultado))
    return resultado


def fourierEf(f,T):
    Ef=lambda t: f(t)**2
    I,e = quad(Ef,0,T)
    return I;

def fourier_a0(f, T):
    f1=lambda t: (1/T)*f(t)
    I,e = quad(f1,0,T)
    return I;


def fourier_an(f, T, n):
    f2 = lambda t : (2/T)*f(t)*np.cos(n*((2*np.pi)/T)*t)
    I,e = quad(f2,0,T)
    return I


def fourier_bn(f, T, n):
    f3 = lambda t : (2/T)*f(t)*np.sin(n*((2*np.pi)/T)*t)
    I,e = quad(f3,0,T)
    return I

def suma_fourier1(f,T,N,t):
    suma = []
    n=1
    while(n<=N):
        suma_parciaT=((fourier_an(f,T,n))*np.cos(n*((2*np.pi)/T)*t)+(fourier_bn(f,T,n)*np.sin(n*((2*np.pi)/T)*t)))
        suma.append(suma_parciaT)
        n+=1
    return suma

def fourier_suma_parciaT(f, T, N):
    res= lambda t:suma_fourier1(f,T,N,t)
    return  lambda t: fourier_a0(f,T) + sum(res(t))

def suma_ice(f,T,t,ef):
    suma = []
    n=1
    salida = False
    while(salida == False):
        suma_parciaT=((fourier_an(f,T,n))*np.cos(n*((2*np.pi)/T)*t)+(fourier_bn(f,T,n)*np.sin(n*((2*np.pi)/T)*t)))
        suma.append(suma_parciaT)
        n+=1
        t2 = np.linspace(-1, 1, 500)
        ploteo = [s(t2) for s in suma]
        comprobacion = sum(ploteo)
        if( comprobacion > 0.02*ef(t2) ):
            salida = True
    return n

def operador_ice(f,T):
    resultado=0
    ef = fourierEf(f,T)
    a0 = fourier_a0(f,T)

    ecuacion_n = lambda t: ef - ( (a0**2)*T + (T/2)* suma_ice(f,T,t,ef))
    print("valor de n para ICE: " + ecuacion_n)
    an = fourier_an(f,T)
    ab = fourier_bn(f,T)








#############################################
#############################################
####DECLARACION DE FUNCIONES PARA APARTADO VISUAL

def ventana_main():
    #configuracion aspectos basicos de ventana
    main_window = tkinter.Tk("pagina principal")
    main_window.geometry("800x700")
    main_window.title("SERIE DE FOURIER TRUNCADA")
    main_window.resizable(False,False)
    #configuracion aspectos basicos de ventana

    #configurando fondo
    bg = tkinter.PhotoImage(file="recursos/sodapdf-converted.png")
    label1 = Label(main_window, image = bg, width=800, height=700)
    label1.place(x=0,y=0)
    #configurando fondo

    ###########################################################################
    #COLOCACION TITULOS

    #se coloca titulo y se centra en pantalla
    prueba = "SERIE DE FOURIER TRUNCADA"
    titulo = Text(main_window,fg="blue",bg="white", height=1, width=29, font=('Helvetica bold',26))
    titulo.tag_configure("tag_titulo", justify="center")
    titulo.insert("1.0", prueba)
    titulo.tag_add("tag_titulo", "1.0", "end")
    titulo.pack()
    #se coloca titulo y se centra en pantalla

    #titulo de resultados
    texto0 = tkinter.Label(main_window, text = "RESULTADOS", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 25")
    texto0.place(x = 290, y = 230)

    #COLOCACION TITULOS
    ############################################################################
    
    
    #####################################################################
    #obtencion de intervalos 1 y valor 1
    data_val1= tkinter.DoubleVar()
    texto1 = tkinter.Label(main_window, text = "Escriba el primer valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto1.place(x = 20, y = 55)
    val1 = tkinter.Entry(main_window, textvariable = data_val1 , width = 5, relief = "flat")
    val1.place(x = 190, y = 55)

    data_incial1= tkinter.DoubleVar()
    texto2 = tkinter.Label(main_window, text = "Escriba los intervalos para el valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto2.place(x = 250, y = 55)
    inicia1 = tkinter.Entry(main_window, textvariable = data_incial1 , width = 5, relief = "flat")
    inicia1.place(x = 490, y = 55)

    texto3 = tkinter.Label(main_window, text = " < t < ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto3.place(x = 520, y = 55)

    data_final1=tkinter.DoubleVar()
    final1 = tkinter.Entry(main_window, textvariable = data_final1 , width = 5, relief = "flat")
    final1.place(x = 555, y = 55)
    #obtencion de intervalos 1 y valor 1
    ###############################################################################

    #####################################################################
    #obtencion de intervalos 2 y valor 2, append a areglos de valores e intervalos
    data_val2=tkinter.DoubleVar()
    texto4 = tkinter.Label(main_window, text = "Escriba el segundo valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto4.place(x = 20, y = 2*55)
    val2 = tkinter.Entry(main_window, textvariable = data_val2 , width = 5, relief = "flat")
    val2.place(x = 198, y = 2*55)

    data_incial2=tkinter.DoubleVar()
    texto5 = tkinter.Label(main_window, text = "Escriba los intervalos para el valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto5.place(x = 250, y = 2*55)
    inicia2 = tkinter.Entry(main_window, textvariable = data_incial2 , width = 5, relief = "flat")
    inicia2.place(x = 490, y = 2*55)

    texto6 = tkinter.Label(main_window, text = " < t < ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto6.place(x = 520, y = 2*55)

    data_final2=tkinter.DoubleVar()
    final2 = tkinter.Entry(main_window, textvariable = data_final2 , width = 5, relief = "flat")
    final2.place(x = 555, y = 2*55)
    #obtencion de intervalos 2 y valor 2
    ###############################################################################

    #####################################################################
    #obtencion de intervalos 3 y valor 3
    data_val3=tkinter.DoubleVar()
    texto7 = tkinter.Label(main_window, text = "Escriba el tercer valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto7.place(x = 20, y = 3*55)
    val3 = tkinter.Entry(main_window, textvariable = data_val3 , width = 5, relief = "flat")
    val3.place(x = 182, y = 3*55)

    data_incial3=tkinter.DoubleVar()
    texto8 = tkinter.Label(main_window, text = "Escriba los intervalos para el valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto8.place(x = 250, y = 3*55)
    inicia3 = tkinter.Entry(main_window, textvariable = data_incial3 , width = 5, relief = "flat")
    inicia3.place(x = 490, y = 3*55)

    texto9 = tkinter.Label(main_window, text = " < t < ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto9.place(x = 520, y = 3*55)

    data_final3=tkinter.DoubleVar()
    final3 = tkinter.Entry(main_window, textvariable = data_final3 , width = 5, relief = "flat")
    final3.place(x = 555, y = 3*55)
    #obtencion de intervalos 3 y valor 3
    ###############################################################################

    ################################################################
    #Configuracion de botones en main_window

    #envia y realiza todos los calculos con los datos recopilados
        #---captura de datos e ingreso en multiples tuplas
    valores_f_array = (data_val1,data_val2,data_final3)
    inciales_f_array = (data_incial1,data_incial2,data_incial3)
    finales_f_array = (data_final1,data_final2,data_final3)
        #--captura de datos e ingreso en multiples tuplas
    botoncalculo = tkinter.Button(main_window, text = "Calcular", command =lambda: accionador_calculador(valores_f_array,inciales_f_array,finales_f_array, main_window), cursor = "hand2", width = 12, relief = "flat")
    botoncalculo.place(x = 600, y = 78)

    #limpia todos los datos de los inputs
    cleaner = tkinter.Button(main_window, text = "Limpiar Datos", command =lambda: clean_data(val1,inicia1,final1,val2,inicia2,final2,val3,inicia3,final3), cursor = "hand2", width = 12, relief = "flat")
    cleaner.place(x = 600, y = 2*68)

    #Configuracion de botones en main_window
    ####################################################################    

    main_window.mainloop()
    
#definicion que limpia los datos de los inputs
def clean_data(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9):
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    print("clean data funcionando!")
    
#def que acciona todos los calculos
def accionador_calculador(array_f,array_inciales,array_finales,ventana):
    print("prueba de array "+ str(array_f[0].get()))
    #------
    #Llama al metodo que calcula el periodo y lo despliega en pantalla
    periodo = calc_periodo(array_inciales[0].get(),array_finales[2].get())
    texto = tkinter.Label(ventana, text = "Periodo", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 270)
    respuesta0 = tkinter.Label(ventana, text = periodo, relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 70, y = 270)
    #Llama al metodo que calcula el periodo y lo despliega en pantalla
    #-----
    #-----
    #recibe un array con los resultados de los coeficientes y lo despliega en pantalla
    array = calc_ice( array_f,array_inciales, array_finales,periodo)
        #-para a0
    texto = tkinter.Label(ventana, text = "Coeficiente A0", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 300)
    respuesta0 = tkinter.Label(ventana, text = array.pop(), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 110, y = 300)
        #-para an
    texto = tkinter.Label(ventana, text = "Coeficiente An", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 330)
    respuesta0 = tkinter.Label(ventana, text = array.pop(), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 110, y = 330)
        #-para bn
    texto = tkinter.Label(ventana, text = "Coeficiente Bn", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 360)
    respuesta0 = tkinter.Label(ventana, text = array.pop(), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 110, y = 360)
    #recibe un array con los resultados de los coeficientes y lo despliega en pantalaa
    #-----
    #-----
    #recibe el valor de N de ICE y lo despliega en pantalla
    #n = calc_ice()
    #texto = tkinter.Label(ventana, text = "Valor de N", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    #texto.place(x = 20, y = 390)
    #respuesta0 = tkinter.Label(ventana, text = n, relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    #respuesta0.place(x = 87, y = 390)
    #recibe el valor de N de ICE y lo despliega en pantalla
    #-----
    #-----
    #-----
    print("accionador calculador funcionando!")


#calcula el periodo "T" de la funcion especificada con los intervalos
def calc_periodo(intervalo_incial, intervalo_final):
    print("intervalo inicial " + str(intervalo_incial))
    print("intervalo final " + str(intervalo_final))
    periodo=0
    while(intervalo_incial < intervalo_final):
        intervalo_incial = intervalo_incial + 1
        periodo = periodo + 1
    return periodo  #duda de si asi se calcula el periodo "periodo/2"

#calcula el valor de los coeficientes de fourier
def calc_ice(array_f,array_inciales, array_finales,T):
    #se construye la funcion
    t = np.linspace(-1, 1, 500)
    funcion_f = buildFunction(array_f,array_inciales,array_finales,t)
    operador_ice(funcion_f,T)

    array = []
    array.append("Ecuacion serie de fourier")
    array.append("coeficiente 3")
    array.append("coeficiente 2")
    array.append("coeficiente 1")
    print("calculo de coeficientes de fourier! ")
    return array



ventana_main()