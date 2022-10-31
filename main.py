#IMPORTS DE LIBRERIAS NECESARIAS
from textwrap import wrap
import tkinter
from tkinter.ttk import Label
from tkinter import *
from tokenize import String
#IMPORTS DE LIBRERIAS NECESARIAS

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

    #se coloca titulo y se centra en pantalla
    prueba = "SERIE DE FOURIER TRUNCADA"
    titulo = Text(main_window,fg="blue",bg="white", height=1, width=29, font=('Helvetica bold',26))
    titulo.tag_configure("tag_titulo", justify="center")
    titulo.insert("1.0", prueba)
    titulo.tag_add("tag_titulo", "1.0", "end")
    titulo.pack()
    #se coloca titulo y se centra en pantalla
    fila1 = generador_textos(main_window,1)
    fila2 = generador_textos(main_window,2)
    fila3 = generador_textos(main_window,3)
    print("fila1 " + str(fila1))
    print("fila2 " + str(fila2))
    print("fila3 " + str(fila3))

    

    main_window.mainloop()
    
def generador_textos(ventana,number):
    resultado = []
    #####################################################################
    #obtencion de intervalos 1 y valor 1
    data_val1=""
    texto1 = tkinter.Label(ventana, text = "Escriba el primer valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto1.place(x = 20, y = number*55)
    val1 = tkinter.Entry(ventana, textvariable = data_val1 , width = 5, relief = "flat")
    val1.place(x = 190, y = number*55)

    data_incial1=""
    texto2 = tkinter.Label(ventana, text = "Escriba los intervalos para el valor de f(t): ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto2.place(x = 250, y = number*55)
    inicia1 = tkinter.Entry(ventana, textvariable = data_incial1 , width = 5, relief = "flat")
    inicia1.place(x = 490, y = number*55)

    texto3 = tkinter.Label(ventana, text = " < t < ", relief = "flat", bg = '#303030', fg = "#FFFFFF", font = "Helvetica 9")
    texto3.place(x = 520, y = number*55)

    data_final1=""
    final1 = tkinter.Entry(ventana, textvariable = data_final1 , width = 5, relief = "flat")
    final1.place(x = 555, y = number*55)
    #obtencion de intervalos 1 y valor 1
    ###############################################################################
    resultado = [data_val1,data_incial1,data_final1]
    return resultado

ventana_main()