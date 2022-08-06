from tkinter import *
from tkinter import ttk
converter = Tk()
converter.title("Unit Converter")
converter.geometry("600x400")

Currencies = {
    "Australian Dollar":54.99,
    "Brazilian Real":15.30,
    "British Pound":95.8,
    "Chinese Yuan":11.74,
    "Euro":80.88,
    "HongKong Dollar":10.11,
    "Indonesian Rupiah":0.005,
    "Japanese Yen":0.587,
    "Pakistani Rupee":0.35,
    "SriLankan Rupee":0.21,
    "Swiss Franc":85.52,
    "Us Dollar":79.37
        }
def convert():
    price = rupees.get()
    answer = variable1.get()
    DICT = Currencies.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ",INSERT,converted)
a = Label(converter,text="Currency Converter",font=("arial",25,"bold","underline"),fg="dark red")
a.place(x=150, y=10)

result = Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
result.place(x=125, y=60)

india = Label(converter,text="Value in indian Rupees:",font=("arial",10,"bold"),fg="red")
india.place(x=30, y=165)

rupees = Entry(converter,font=("arial",20))
rupees.place(x=200, y=160)

choice = Label(converter,text="Choice:",font=("arial",10,"bold"),fg="red")
choice.place(x=30, y=220)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter,variable1,*Currencies)
option.place(x=100 , y=210,width=100, height=40)

button = Button(converter,text="Convert",fg="green",font=("arial",20),bg="powder blue",command=convert)
button.place(x=200, y=210,height=40,width=150)
converter.mainloop()