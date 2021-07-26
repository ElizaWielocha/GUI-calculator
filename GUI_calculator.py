# GUI calculator aplication

from tkinter import *

# okno - wyglad
calc = Tk()
calc.title("CALCULATOR")
calc.geometry("354x460")
calc.config(background = "pink")
calc.iconbitmap("calc.ico")

# poczatkowy napis
start = Label(calc, text = "CALCULATOR", bg = "white", font = ("Arial", 30, 'bold'))
start.pack(side = TOP)

calculation = StringVar()
operator = ""

# funkcje
def clicknum(number):  #do wpisywania numerow i zapisywania rownan
    global operator 
    operator = operator + str(number)
    calculation.set(operator)

def equal():   # funkcja zliczajaca i podajaca wynik
    global operator
    score = str(eval(operator))
    calculation.set(score)
    operator = ''

def CE():   # funkcja czysczaca
    global operator
    calculation.set('')

#okienko na obliczenia
mytext = Entry(calc, textvariable = calculation, width = 25, bd = 5, bg = 'white')
mytext.pack()

#guziki
butt1 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(1), text = "1", )
butt1.place( x = 10, y = 100)

butt2 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(2), text = "2", )
butt2.place( x = 10, y = 170)

butt3 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(3), text = "3", )
butt3.place( x = 10, y = 240)

butt4 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(4), text = "4", )
butt4.place( x = 75, y = 100)

butt5 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(5), text = "5", )
butt5.place( x = 75, y = 170)

butt6 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(6), text = "6", )
butt6.place( x = 75, y = 240)

butt7 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(7), text = "7", )
butt7.place( x = 140, y = 100)

butt8 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(8), text = "8", )
butt8.place( x = 140, y = 170)

butt9 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(9), text = "9", )
butt9.place( x = 140, y = 240)

butt0 = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum(0), text = "0", )
butt0.place( x = 10, y = 310)

buttdot = Button(calc, padx = 47, pady = 14, bd = 4, bg = "white", command = lambda:clicknum('.'), text = ".", )
buttdot.place( x = 75, y = 310)

buttplus = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum('+'), text = "+", )
buttplus.place( x = 205, y = 100)

buttminus = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum('-'), text = "-", )
buttminus.place( x = 205, y = 170)

buttstar = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum('*'), text = "*", )
buttstar.place( x = 205, y = 240)

buttslash = Button(calc, padx = 14, pady = 14, bd = 4, bg = "white", command = lambda:clicknum('/'), text = "/", )
buttslash.place( x = 205, y = 310)

buttCE = Button(calc, padx = 20, pady = 119, bd = 4, bg = "white", command = CE, text = "CE", )
buttCE.place( x = 270, y = 100)

buttequal = Button(calc, padx = 153, pady = 20, bd = 4, bg = "white", command = equal, text = "=", )
buttequal.place( x = 10, y = 380)


calc.mainloop()
