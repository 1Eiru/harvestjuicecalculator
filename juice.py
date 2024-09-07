import requests
from tkinter import *
from PIL import Image, ImageTk
import os
import math

url = 'https://api.poe.watch/get?category=currency&league=Settlers'
response = requests.get(url)
print(response)
id = 56327
data = response.json()
mean_value = 0

for items in data:
    if items['id'] == id:
        mean_value = items['mean']


   
main_w = Tk(screenName="Juice")
main_w.title("Juize")
divine_orb_image = PhotoImage(file="divineorb.png")
main_w.iconbitmap("orb.ico")
chaos_image = PhotoImage(file="chaos.png")
vividimg = PhotoImage(file="vivid icon.png")
primalimg = PhotoImage(file="primal icon.png")
wildimg = PhotoImage(file="wild icon.png")
main_w.maxsize(300, 350)
main_w.minsize(300, 350)
divine = StringVar()
divine_input = Entry(main_w, text=divine, width=5)
divine_input.grid(row=1, column=0, pady=6)

divine_label = Label(main_w, text='=', image=divine_orb_image, compound=LEFT)
divine_label.grid(row=0)

chaos_label = Label(main_w, image=chaos_image, compound=RIGHT)
chaos_label.grid(column=1, row=0)

vivid = StringVar()
vivid_label = Label(main_w,text="._.",image=vividimg,compound=LEFT)
vivid_label.grid(column=0, row=2)
vividprice1 = Label(main_w,text="._.",compound=LEFT)
vividprice1.grid(row=2, column= 1)
vivid2 = StringVar()
vivid_input = Entry(main_w, text=vivid, width=10)
vivid_input.grid(row=3, column=0)
vivid_input2 = Entry(main_w,text=vivid2, width=5)
vivid_input2.grid(row=3, column=1)


wild = StringVar()
wild_label = Label(main_w, text="._.",image= wildimg, compound= LEFT)
wild_label.grid(column=0, row=4)
wildprice1 = Label(main_w,text="._.",compound=LEFT)
wildprice1.grid(row=4, column= 1)
wild2 = StringVar()
wild_input = Entry(main_w, text=wild, width=10)
wild_input.grid(row=5, column=0)
wild_input2 = Entry(main_w, text=wild2, width=5)
wild_input2.grid(row=5, column=1)

primal = StringVar()
primal_label = Label(main_w,text="._.", image= primalimg, compound= LEFT)
primal_label.grid(column=0, row=6)
primalprice1 = Label(main_w,text="._.",compound=LEFT)
primalprice1.grid(row=6, column= 1)
primal2 = StringVar()
primal_input = Entry(main_w, text=primal, width=10)
primal_input.grid(row=7, column=0)
primal_input2 = Entry(main_w, text=primal2, width=5)
primal_input2.grid(row=7, column=1)

def callitcuh(var, index, mode):
    whole_mean = int(mean_value)
    try:
        divine_int = float(divine_input.get())
        fraction , whole = math.modf(divine_int)
        fraction = round(fraction, 2)
        coc = (whole * int(mean_value)) + (whole_mean * fraction)
        text1 = coc
    except ValueError:
        text1 = "intfloatdoubleonle:>!"
    chaos_label.config(text=text1)

def wildlife(var, index, mode):
    try:
        wildprice = int(wild_input.get()) / int(wild_input2.get())
        wildexact = int(wildprice) * int(wild_input2.get())
        wild_label.config(text=wildexact)
        intwildprice = int(wildprice)
        text1 = wildexact
        text2 = intwildprice
    except ValueError:
        text1 = "!!!"
        text2 = "!!!"
    wild_label.config(text=text1)
    wildprice1.config(text=f"| {text2}")

def wildlife2(var, index, mode):
    try:
        wildprice = int(wild_input.get()) / int(wild_input2.get())
        wildexact = int(wildprice) * int(wild_input2.get())
        wild_label.config(text=wildexact)
        intwildprice = int(wildprice)
        text1 = wildexact
        text2 = intwildprice
    except ValueError:
        text1 = "!!!"
        text2 = "!!!"
    wild_label.config(text=text1)
    wildprice1.config(text=f"| {text2}")

def vividlife(var, index, mode):
    try:
        vividprice = int(vivid_input.get()) / int(vivid_input2.get())
        vividexact = int(vividprice) * int(vivid_input2.get())
        intvividprice = int(vividprice)
        text1 = vividexact
        text2 = intvividprice
    except ValueError:
        text1 = "!!!"
        text2 = "!!!"
    vivid_label.config(text=text1)
    vividprice1.config(text=f"| {text2}")

def vividlife2(var, index, mode):
    try:
        vividprice = int(vivid_input.get()) / int(vivid_input2.get())
        vividexact = int(vividprice) * int(vivid_input2.get())
        intvividprice = int(vividprice)
        text1 = vividexact
        text2 = intvividprice
    except ValueError:
        text1 = "!!!"
        text2 = "!!!"
    vivid_label.config(text=text1)
    vividprice1.config(text=f"| {text2}")

def primallife(var, index, mode):
    try:
        primalprice = int(primal_input.get()) / int(primal_input2.get())
        primalexact = int(primalprice) * int(primal_input2.get())
        intprimalprice = int(primalprice)
        text1 = primalexact
        text2 = intprimalprice
    except ValueError:
        text1 = "!!!"
        text2 = "!!!"
    primal_label.config(text=text1)
    primalprice1.config(text=f"| {text2}")

def primallife2(var, index, mode):
    try:
        primalprice = int(primal_input.get()) / int(primal_input2.get())
        primalexact = int(primalprice) * int(primal_input2.get())
        intprimalprice = int(primalprice)
        text1 = primalexact
        text2 = intprimalprice
    except ValueError:
        text1 = "!!!"
        text2 = "!!!"
    primal_label.config(text=text1)
    primalprice1.config(text=f"| {text2}")

divine.trace("w", callitcuh)
primal.trace("w", primallife)
primal2.trace("w", primallife)
vivid.trace("w", vividlife)
vivid2.trace("w", vividlife)
wild.trace("w", wildlife)
wild2.trace("w", wildlife)
main_w.mainloop()





# 110 ×

# 0.1 div ⇒ 11 c
# 0.2 div ⇒ 22 c
# 0.3 div ⇒ 33 c
# 0.4 div ⇒ 44 c
# 0.5 div ⇒ 55 c
# 0.6 div ⇒ 66 c
# 0.7 div ⇒ 77 c
# 0.8 div ⇒ 88 c
# 0.9 div ⇒ 99 c