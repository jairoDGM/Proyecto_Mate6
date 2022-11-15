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
from sympy import *
import sympy as sym
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


def fourierEf(array_f,T):
    t = sym.Symbol('t')
    funcion1= "("+str(array_f[0].get())+")" + "**2"
    funcion2= "("+str(array_f[1].get())+")" + "**2"
    funcion3= "("+str(array_f[2].get())+")" + "**2"
    
    print("valor de perido: " + str(T))
    print("funcion1: " + funcion1)
    print("funcion2: " + funcion2)
    print("funcion3: " + funcion3)
    I1 = sym.integrate(funcion1, (t,0,T))
    I2 = sym.integrate(funcion2, (t,0,T))
    I3 = sym.integrate(funcion3, (t,0,T))
    #I1,e = quad(lambda t:funcion1,0,T)
    #I2,e = quad(lambda t: funcion2,0,T)
    #I3,e = quad(lambda t: funcion3,0,T)
    print("############################")
    print("integral 1: " + str(I1))
    print("integral 1: " + str(I2))
    print("integral 1: " + str(I3))
    respuesta = I1 + I2 + I3
    return respuesta;

def fourier_a0(f, T):
    contador = 0
    I = []
    while(contador<=2):
        f1 = f[contador].get()
        t = sym.Symbol('t')
        ecuacion= str(1/T) + "*" + str(f1)
        I.append(sym.integrate(ecuacion,(t,0,T)))
        contador = contador + 1
    
    return sum(I)


def fourier_an(f, T, n):
    contador = 0
    I = []
    while(contador <= 2):
        f2 = f[contador].get()
        t = sym.Symbol('t')
        argumento = n*((2*np.pi)/T)
        ecuacion = str(2/T) + "*" + str(f2) + "*" + "(cos(" + str(argumento) + "*t))"
        print("INTEGRAL AN: "+ecuacion+ " DE: " + str(f2))
        operacion = sym.integrate(ecuacion,(t,0,T))
        I.append(operacion)
        contador = contador + 1
    
    return sum(I)


def fourier_bn(f, T, n):
    contador = 0
    I = []
    while(contador <= 2):
        f3 = f[contador].get()
        t = sym.Symbol('t')
        argumento = n*((2*np.pi)/T)
        ecuacion = str(2/T)+"*"+str(f3)+"*"+"(sin("+str(argumento)+"*t))"
        print("INTEGRAL ARMADA BN: "+ecuacion+" DE: " + str(f3))
        I.append(sym.integrate(ecuacion,(t,0,T)))
        contador = contador + 1

    return sum(I)


def suma_ice(f,T,ef,pam1,a0,valor_n):
    suma = []
    n=1
    suma_parciaT = 0
    while(n <= valor_n.get()):
        t = sym.Symbol('t')
        parte1 = fourier_an(f,T,n)
        parte2= fourier_bn(f,T,n)
        print("PARTE 1: " + str(parte1))
        print("PARTE2: " + str(parte2))
        suma_parciaT = pam1*(parte1 + parte2)
        suma.append(suma_parciaT)
        n+=1

        ecuacion = ef - ( (a0**2)*T + sum(suma))
        print("SUMA REALIZADA: " + str(ecuacion))

        print("VALOR LIMITE"+str(0.02*ef))
        
    return n-1

def sft_constructor(array_result,T):
    t = sym.Symbol('t')
    n=1
    sigma=0
    while(n <= array_result[4]):
        argumento1 = t*(n*2*np.pi/T)
        parte1= array_result[2]*sym.cos(argumento1)
        parte2 = array_result[3]*sym.sin(argumento1)
        sigma = sigma + (parte1 + parte2)
        n+=1
    sigma = sigma + array_result[1]
    return sigma


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
    data_val1= tkinter.StringVar()
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
    data_val2=tkinter.StringVar()
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
    data_val3=tkinter.StringVar()
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

    valor_n=tkinter.DoubleVar()
    texto7 = tkinter.Label(main_window, text = "Escriba el valor de n deseado de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto7.place(x = 20, y = 3*55 + 30)
    val3 = tkinter.Entry(main_window, textvariable = valor_n , width = 5, relief = "flat")
    val3.place(x = 227, y = 3*55 + 30)
    #obtencion de intervalos 3 y valor 3
    ###############################################################################

    ################################################################
    #Configuracion de botones en main_window

    #envia y realiza todos los calculos con los datos recopilados
        #---captura de datos e ingreso en multiples tuplas
    valores_f_array = (data_val1,data_val2,data_val3)
    inciales_f_array = (data_incial1,data_incial2,data_incial3)
    finales_f_array = (data_final1,data_final2,data_final3)
        #--captura de datos e ingreso en multiples tuplas
    botoncalculo = tkinter.Button(main_window, text = "Calcular", command =lambda: accionador_calculador(valor_n,valores_f_array,inciales_f_array,finales_f_array, main_window), cursor = "hand2", width = 12, relief = "flat")
    botoncalculo.place(x = 600, y = 78)

    #limpia todos los datos de los inputs
    cleaner = tkinter.Button(main_window, text = "Limpiar Datos", command =lambda: clean_data(val1,inicia1,final1,val2,inicia2,final2,val3,inicia3,final3,valor_n), cursor = "hand2", width = 12, relief = "flat")
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
def accionador_calculador(valor_n,array_f,array_inciales,array_finales,ventana):
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
    array = calc_ice( valor_n,array_f,array_inciales, array_finales,periodo)
        #-para a0
    texto = tkinter.Label(ventana, text = "Coeficiente A0", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 300)
    respuesta0 = tkinter.Label(ventana, text = str(array[1]), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 110, y = 300)
        #-para an
    texto = tkinter.Label(ventana, text = "Coeficiente An", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 330)
    respuesta0 = tkinter.Label(ventana, text = str(array[2]), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 110, y = 330)
        #-para bn
    texto = tkinter.Label(ventana, text = "Coeficiente Bn", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 360)
    respuesta0 = tkinter.Label(ventana, text = str(array[3]), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 110, y = 360)
    #recibe un array con los resultados de los coeficientes y lo despliega en pantalaa
    #-----
    #-----
    #recibe el valor de N de ICE y lo despliega en pantalla
    texto = tkinter.Label(ventana, text = "Valor de N", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 390)
    respuesta0 = tkinter.Label(ventana, text = str(array[4]), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 87, y = 390)
    #recibe el valor de N de ICE y lo despliega en pantalla
    #-----
    #-----
    sft = sft_constructor(array,periodo)
    texto = tkinter.Label(ventana, text = "Valor del SFT Final: ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 10")
    texto.place(x = 20, y = 450)
    respuesta0 = tkinter.Label(ventana, text = str(sft), relief = "flat", bg = '#1F618D', fg = "#17202A", font = "Helvetica 10")
    respuesta0.place(x = 20, y = 470)
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
    return periodo  

#calcula el valor de los coeficientes de fourier
def calc_ice(valor_n,array_f,array_inciales, array_finales,T):
    resultado=[]
    ef=fourierEf(array_f,T)
    a0 = fourier_a0(array_f,2)


    print("integral de energia: " + str(ef))
    print("PRUEBA A0: " + str(a0))
    print("########################################")
    #obtiene el n necesario para calcular los coeficientes
    ecuacion = suma_ice(array_f,T,ef,(T/2),a0,valor_n)

    #calculos con el valor de N obtenido
    an = fourier_an(array_f,T,ecuacion)
    bn = fourier_bn(array_f,T,ecuacion)

    resultado.append(ef)
    resultado.append(a0)
    resultado.append(an)
    resultado.append(bn)
    resultado.append(ecuacion)
    return resultado

ventana_main()