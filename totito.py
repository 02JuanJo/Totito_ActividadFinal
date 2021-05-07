#----------------------------------------------------------#
# Importanción de librerías que se ocuparán en la actividad.
from tkinter import *
from tkinter import messagebox
#----------------------------------------------------------#

#----------------------------------------------------------#
# Creación de la ventana principal y su título.
root = Tk()
root.title('Totito - Actividad Lab')
#----------------------------------------------------------#

#----------------------------------------------------------#
# Inicialización de las variables.
turno_X = True 
cuenta_turnos = 0 
#----------------------------------------------------------#

#----------------------------------------------------------#
# Revisión general si existe un ganador durante el juego.

def revisar_ganador_X():
    global ganador
    ganador = False

    #--------------------------Se revisa la Primera fila--------------------------------#
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":

        #Si se cumplen las condiciones se cambia el color.
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

        
    #--------------------------Se revisa la Segunda fila--------------------------------#
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":

        #Si se cumplen las condiciones se cambia el color.
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Tercera fila--------------------------------#
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":

        #Si se cumplen las condiciones se cambia el color.
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Primera columna--------------------------------#
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":

        #Si se cumplen las condiciones se cambia el color.
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Segunda columna--------------------------------#
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":

        #Si se cumplen las condiciones se cambia el color.
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Tercera columna--------------------------------#
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":

        #Si se cumplen las condiciones se cambia el color.
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Diagonal menor--------------------------------#
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        #Si se cumplen las condiciones se cambia el color.
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Diagonal mayor--------------------------------#
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        #Si se cumplen las condiciones se cambia el color.
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

def revisar_ganador_O():
    global ganador
    ganador = False

    #--------------------------Se revisa la Primera fila--------------------------------#
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":

        #Si se cumplen las condiciones se cambia el color.
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "O gana")
        #Y se resetea el juego.
        resetear()

        
    #--------------------------Se revisa la Segunda fila--------------------------------#
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":

        #Si se cumplen las condiciones se cambia el color.
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "O gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Tercera fila--------------------------------#
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":

        #Si se cumplen las condiciones se cambia el color.
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "O gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Primera columna--------------------------------#
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":

        #Si se cumplen las condiciones se cambia el color.
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "O gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Segunda columna--------------------------------#
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":

        #Si se cumplen las condiciones se cambia el color.
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "X gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Tercera columna--------------------------------#
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":

        #Si se cumplen las condiciones se cambia el color.
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "O gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Diagonal menor--------------------------------#
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        #Si se cumplen las condiciones se cambia el color.
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "O gana")
        #Y se resetea el juego.
        resetear()

    #--------------------------Se revisa la Diagonal mayor--------------------------------#
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        #Si se cumplen las condiciones se cambia el color.
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")

        #El ganador se encontró, por lo que el flag cambia su estado.
        ganador = True

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "O gana")
        #Y se resetea el juego.
        resetear()

def revisar_empate():
    global ganador
    ganador = False

    #Si no se encuentra alguna confirmación de ganador se procede a empate.

    if cuenta_turnos == 9 and ganador == False:

        #Si se cumplen las condiciones se cambia el color.
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")

        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")

        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")

        #Y por último se notifica que se encontró ganador.
        messagebox.showinfo("Game Over", "Empate")
        #Y se resetea el juego.
        resetear()

#----------------------------------------------------------#
# Selección de turnos

def seleccion_turno(boton):
    global turno_X, cuenta_turnos

    if boton["text"] == " " and turno_X == True:

        #Si el turno es de las X, se setea el texto del botón a X.
        boton["text"] = "X"

        #Se cambia el turno.
        turno_X = False

        #Aumentan los turnos realizados.
        cuenta_turnos += 1

        #Y se procede a revisar si hay algun ganador.
        revisar_ganador_X()
        revisar_ganador_O()
        revisar_empate()
        #En el caso que no exista ganador, continua la 
        #ejecución del programa hasta encontrar alguno.

    elif boton["text"] == " " and turno_X == False:

        #Si el turno es de las O, se setea el texto del botón a O.
        boton["text"] = "O"

        #Se cambia el turno.
        turno_X = True

        #Aumentan los turnos realizados.
        cuenta_turnos += 1

        #Y se procede a revisar si hay algun ganador.
        revisar_ganador_X()
        revisar_ganador_O()
        revisar_empate()
        #En el caso que no exista ganador, continua la 
        #ejecución del programa hasta encontrar alguno.

    else:

        #Si por algún motivo, el usuario intenta realizar un click
        #en un botón ya modificado, no pasará nada y la opción no cambiará.
        pass

#----------------------------------------------------------#
# Seteo al inicio y fin de cada juego.

def resetear():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global turno_X, cuenta_turnos
    turno_X = True
    cuenta_turnos = 0

    #----------------------------------------------------------#
    # Creación de cada botón en la cuadrícula 3x3
    b1 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b1))
    b2 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b2))
    b3 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b3))

    b4 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b4))
    b5 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b5))
    b6 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b6))

    b7 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b7))
    b8 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b8))
    b9 = Button(root, text=" ", height=6, width=10, command=lambda: seleccion_turno(b9))
    #----------------------------------------------------------#

    #----------------------------------------------------------#
    # Creación de la cuadrícula 3x3 por medio de coordenadas.
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    #----------------------------------------------------------#

#----------------------------------------------------------#

resetear()
root.mainloop()