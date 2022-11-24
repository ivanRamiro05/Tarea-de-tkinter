import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

x = np.linspace(-5, 5, 1000)

# graficar funciones
def configuracion_grafico(): 
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Calculadora graficadora")
    plt.grid()
    plt.axhline(y=0, color="b")
    plt.axvline(x=0, color="b")
    plt.show()

def funcion_g1():
    y = float(g1_a.get()) * x + float(g1_b.get())
    plt.style.use('dark_background')
    plt.plot(x, y, color="r")
    configuracion_grafico()

def funcion_g2():
    y = float(g2_a.get()) * x**2 + float(g2_b.get()) * x + float(g2_c.get())
    plt.style.use('dark_background')
    plt.plot(x, y, color="r")
    configuracion_grafico()

def funcion_g3():
    y = float(g3_a.get()) * x**3 + float(g3_b.get()) * x**2 + float(g3_c.get()) * x + float(g3_d.get())
    plt.style.use('dark_background')
    plt.plot(x, y, color="r")
    configuracion_grafico()

def funcion_ex():
    y = float(ex_a.get()) ** x
    plt.style.use('dark_background')
    plt.plot(x, y, color="r")
    configuracion_grafico()
  
def funcion_log():
    y = np.log(x) / np.log(float(log_a.get()))
    plt.style.use('dark_background')
    plt.plot(x, y, color="r")
    configuracion_grafico()

root = Tk()
root.config(bg="#8A8A8A")

# a, b, c y d
atext = Label(root, text="a")
atext.grid(row=0, column=1)

btext = Label(root, text="b")
btext.grid(row=0, column=2)

ctext = Label(root, text="c")
ctext.grid(row=0, column=3)

btext = Label(root, text="d")
btext.grid(row=0, column=4)

# función g1
label_g1 = Label(root, text="y = ax + b")
label_g1.grid(row=0, column=0)
graficar_g1 = Button(root, text="Graficar", command=funcion_g1)
graficar_g1.grid(row=1, column=0)

g1_a = Entry(root, width=5)
g1_a.grid(row=1, column=1, padx=5)

g1_b = Entry(root, width=5)
g1_b.grid(row=1, column=2, padx=5)

# función g2
label_g2 = Label(root, text="y = ax² + bx + c")
label_g2.grid(row=2, column=0)
graficar_g2 = Button(root, text="Graficar", command=funcion_g2)
graficar_g2.grid(row=3, column=0)

g2_a = Entry(root, width=5)
g2_a.grid(row=3, column=1, padx=5)

g2_b = Entry(root, width=5)
g2_b.grid(row=3, column=2, padx=5)

g2_c = Entry(root, width=5)
g2_c.grid(row=3, column=3, padx=5)

# función g3
label_g3 = Label(root, text="y = ax³ + bx² + c")
label_g3.grid(row=4, column=0)
graficar_g3 = Button(root, text="Graficar", command=funcion_g3)
graficar_g3.grid(row=5, column=0)

g3_a = Entry(root, width=5)
g3_a.grid(row=5, column=1, padx=5)

g3_b = Entry(root, width=5)
g3_b.grid(row=5, column=2, padx=5)

g3_c = Entry(root, width=5)
g3_c.grid(row=5, column=3, padx=5)

g3_d = Entry(root, width=5)
g3_d.grid(row=5, column=4, padx=5)

# funcion ex
label_ex = Label(root, text="y = a^x")
label_ex.grid(row=6, column=0)
graficar_ex = Button(root, text="Graficar", command=funcion_ex)
graficar_ex.grid(row=7, column=0)

ex_a = Entry(root, width=5)
ex_a.grid(row=7, column=1, padx=5)

# funcion log
label_ex = Label(root, text="y = logₐ(x)")
label_ex.grid(row=8, column=0)
graficar_ex = Button(root, text="Graficar", command=funcion_log)
graficar_ex.grid(row=9, column=0)

log_a = Entry(root, width=5)
log_a.grid(row=9, column=1, padx=5)

root.mainloop()
