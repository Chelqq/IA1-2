import tkinter.tix
from tkinter import *
from tkinter import messagebox
from tkinter import tix
from tkinter import ttk
from tkinter.constants import *
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

distances = []
fares = []
data = {}

window = tix.Tk()
window.title("Regresion lineal")
window.geometry("1200x600")

tip = tkinter.tix.Balloon(window)
fig = plt.figure()

def add():
      if txtdistance.get() in distances:
         i = distances.index(txtdistance.get())
         distances[i] = txtdistance.get()
         fares[i] = txtfare.get()
      else:
         distances.append(txtdistance.get())
         fares.append(txtfare.get())
      updatelists()
      plot()

def new():
    distances.clear()
    fares.clear()

    lstdistance.delete(0, END)
    lstfare.delete(0, END)
    lstdistance.delete(0, END)
    lstpredfare.delete(0, END)
    txtslope.delete(0, END)
    txtintercept.delete(0, END)
    showGraph()

def updatelists():
      lstdistance.delete(0,END)
      lstfare.delete(0,END)
      for distance in distances:
           lstdistance.insert(END,distance)
      for fare in fares:
           lstfare.insert(END,fare)

def mouseEvent(event):
    distances.append(round(event.xdata, 2))
    fares.append(round(event.ydata, 2))
    updatelists()


def plot():
    data["distances"] = distances
    data["fares"] = fares

    df = pd.DataFrame(data)
    X = df[["distances"]]
    y = df["fares"]

    model = LinearRegression()
    model.fit(X, y)

    y_pred = model.predict(X)

    lstpredfare.delete(0, END)
    for n in y_pred:
        lstpredfare.insert(END, n)

    txtintercept.delete(0, END)
    txtintercept.insert(0, str(round(model.intercept_, 2)))

    txtslope.delete(0, END)
    txtslope.insert(0, str(round(model.coef_[0], 2)))

    clearplot()

    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)

    ax.plot(X, y, color="red", marker="o", markerfacecolor="blue", label="Linea actual")
    ax.plot(X, y_pred, color="blue", marker="o", markerfacecolor="blue", label="Regresion predecida")
    ax.set_title("Regresion lineal")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

def showGraph():

    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
    cid = fig.canvas.mpl_connect('button_press_event', mouseEvent)

    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)

    ax.set_title("Regresion lineal")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

def clearplot():
  for widget in window.winfo_children():
       if "Canvas" in str(type(widget)):
          widget.destroy()

def listselected(event):
  if len(lstdistance.curselection()) == 0:
     return
  i = lstdistance.curselection()[0]
  txtdistance.delete(0,END)
  txtdistance.insert(END,distances[i])
  txtfare.delete(0,END)
  txtfare.insert(END,fares[i])


btnplot = Button(window,text="Plot",command=plot)
btnplot.place(x=50,y=50,width=200)

btndelete = Button(window,text="New",command=new)
btndelete.place(x=50,y=100,width=100)

btnclear = Button(window,text="Clear",command=clearplot)
btnclear.place(x=150,y=100,width=100)

txtX = Label(window,text="X",anchor="w")
txtX.place(x=80,y=150,width=65)

lstdistance = Listbox(window)
lstdistance.place(x=50,y=175,width=65)

txtY = Label(window,text="Y",anchor="w")
txtY.place(x=150,y=150,width=65)

lstfare = Listbox(window)
lstfare.place(x=120,y=175,width=65)

txtYPred = Label(window,text="Y Pred",anchor="w")
txtYPred.place(x=200,y=150,width=65)

lstpredfare = Listbox(window)
lstpredfare.place(x=190,y=175,width=65)

lblintercept = Label(window,text="Interceptar Y: ",anchor="w")
lblintercept.place(x=50,y=400,width=100)

txtintercept = Entry(window)
txtintercept.place(x=150,y=400,width=100)

lblslope = Label(window,text="Pendiente: ",anchor="w")
lblslope.place(x=50,y=430,width=100)

txtslope = Entry(window)
txtslope.place(x=150,y=430,width=100)

lstdistance.bind("<<ListboxSelect>>",listselected)

tip.bind_widget(lstdistance,balloonmsg="X")
tip.bind_widget(lstfare,balloonmsg="Linea actual")
tip.bind_widget(lstpredfare,balloonmsg="Regresion prevista")

showGraph()
window.mainloop()