from asyncio.windows_events import NULL
from tkinter import *
from rootMetods import *
from integMetods import *
from systemMetods import *


def SpawnMainMenu():
    mainMenu=Frame(root)
    mainMenu.grid(row=0,column=0)

    method_label = Label(mainMenu, text="Выберите метод:",font=500)
    method_label.grid(row=0,column=1)


    entries_frame = Frame(mainMenu)
    entries_frame.grid(row=1,column=1,pady=100)

    inLable=Label(entries_frame,text="нахождение корня уравнения",font=250)
    inLable.grid(row=0,column=2,pady=25)
    solve_button = Button(entries_frame, text="метод половиного деления",font=125, command=lambda:LoadMenu(1,0))
    solve_button.grid(row=1,column=0,padx=100)
    solve_button = Button(entries_frame, text="метод хорд",font=125, command=lambda:LoadMenu(1,1))
    solve_button.grid(row=1,column=1,padx=100)
    solve_button = Button(entries_frame, text="метод касательных",font=125, command=lambda:LoadMenu(1,2))
    solve_button.grid(row=1,column=3,padx=100)
    solve_button = Button(entries_frame, text="метод хорд и касательных",font=125, command=lambda:LoadMenu(1,3))
    solve_button.grid(row=1,column=4,padx=100)

    entries_frame = Frame(mainMenu)
    entries_frame.grid(row=2,column=1,pady=100)
    inLable=Label(entries_frame,text="нахождение определеного интеграла",font=250)
    inLable.grid(row=0,column=1,pady=25)
    solve_button = Button(entries_frame, text="метод прямокгольников",font=125, command=lambda:LoadMenu(2,0))
    solve_button.grid(row=1,column=0,padx=100)
    solve_button = Button(entries_frame, text="метод прапеции",font=125, command=lambda:LoadMenu(2,1))
    solve_button.grid(row=1,column=1,padx=100)
    solve_button = Button(entries_frame, text="метод симпсона",font=125, command=lambda:LoadMenu(2,2))
    solve_button.grid(row=1,column=2,padx=100)

    entries_frame = Frame(mainMenu)
    entries_frame.grid(row=3,column=1,pady=100)
    inLable=Label(entries_frame,text="нахождение решения системы уравнений",font=250)
    inLable.grid(row=0,column=2,pady=25)
    solve_button = Button(entries_frame, text="метод эйлера",font=125, command=lambda:LoadMenu(3,0))
    solve_button.grid(row=1,column=1,padx=100)
    solve_button = Button(entries_frame, text="метод рунге-кутта",font=125, command=lambda:LoadMenu(3,1))
    solve_button.grid(row=1,column=3,padx=100)

    return mainMenu

def SpawnRootFXMenu(method):
    RootFXMenu=Frame(root)
    RootFXMenu.grid(row=0,column=0,padx=150,pady=150)

    inLable=Button(RootFXMenu,text="<",font=250,command=lambda:LoadMenu(0))
    inLable.grid(row=0,column=0,pady=25)

    method_label1 = Label(RootFXMenu, text="Введите данные",font=500)
    method_label1.grid(row=0,column=1,pady=25)

    method_label = Label(RootFXMenu, text="уравнение:",font=500)
    method_label.grid(row=1,column=0,pady=10)
    method_Enter1=Entry(RootFXMenu,textvariable="")
    method_Enter1.grid(row=1,column=1,pady=10)

    method_label = Label(RootFXMenu, text="a:",font=500)
    method_label.grid(row=2,column=0,pady=10)
    method_Enter2=Entry(RootFXMenu,textvariable="")
    method_Enter2.grid(row=2,column=1,pady=10)

    method_label = Label(RootFXMenu, text="b:",font=500)
    method_label.grid(row=3,column=0,pady=10)
    method_Enter3=Entry(RootFXMenu,textvariable="")
    method_Enter3.grid(row=3,column=1,pady=10)

    method_label = Label(RootFXMenu, text="e:",font=500)
    method_label.grid(row=4,column=0,pady=10)
    method_Enter4=Entry(RootFXMenu,textvariable="")
    method_Enter4.grid(row=4,column=1,pady=10)

    method_Enter=Button(RootFXMenu,text="calculate",command=lambda:DoMethod(CalculateRoot(method_Enter1.get(),float(method_Enter2.get()),float(method_Enter3.get()),float(method_Enter4.get()),method),RootFXMenu))
    method_Enter.grid(row=5,column=1)

    return RootFXMenu

def SpawnIntegFXMenu(m):
    RootFXMenu=Frame(root)
    RootFXMenu.grid(row=0,column=0,padx=150,pady=150)

    inLable=Button(RootFXMenu,text="<",font=250,command=lambda:LoadMenu(0))
    inLable.grid(row=0,column=0,pady=25)

    method_label1 = Label(RootFXMenu, text="Введите данные",font=500,name="txt")
    method_label1.grid(row=0,column=1,pady=25)

    method_label = Label(RootFXMenu, text="подинтегральное выражение:",font=500)
    method_label.grid(row=1,column=0,pady=10)
    method_Enter1=Entry(RootFXMenu,textvariable="")
    method_Enter1.grid(row=1,column=1,pady=10)

    method_label = Label(RootFXMenu, text="a:",font=500)
    method_label.grid(row=2,column=0,pady=10)
    method_Enter2=Entry(RootFXMenu,textvariable="")
    method_Enter2.grid(row=2,column=1,pady=10)

    method_label = Label(RootFXMenu, text="b:",font=500)
    method_label.grid(row=3,column=0,pady=10)
    method_Enter3=Entry(RootFXMenu,textvariable="")
    method_Enter3.grid(row=3,column=1,pady=10)

    method_label = Label(RootFXMenu, text="k:",font=500)
    method_label.grid(row=4,column=0,pady=10)
    method_Enter4=Entry(RootFXMenu,textvariable="")
    method_Enter4.grid(row=4,column=1,pady=10)

    method_label = Label(RootFXMenu, text="e:",font=500)
    method_label.grid(row=5,column=0,pady=10)
    method_Enter5=Entry(RootFXMenu,textvariable="")
    method_Enter5.grid(row=5,column=1,pady=10)

    method_Enter=Button(RootFXMenu,text="calculate",command=lambda:DoMethod(CalculateInteg(method_Enter1.get(),float(method_Enter2.get()),float(method_Enter3.get()),int(method_Enter4.get()),float(method_Enter5.get()),m),RootFXMenu))
    method_Enter.grid(row=6,column=1)

    return RootFXMenu

def SpawnSystemFXMenu(method):
    RootFXMenu=Frame(root)
    RootFXMenu.grid(row=0,column=0,padx=150,pady=150)

    inLable=Button(RootFXMenu,text="<",font=250,command=lambda:LoadMenu(0))
    inLable.grid(row=0,column=0,pady=25)

    method_label1 = Label(RootFXMenu, text="Введите данные",font=500)
    method_label1.grid(row=0,column=1,pady=25)

    method_label = Label(RootFXMenu, text="f(x,y):",font=500)
    method_label.grid(row=1,column=0,pady=10)
    method_Enter1=Entry(RootFXMenu,textvariable="")
    method_Enter1.grid(row=1,column=1,pady=10)

    method_label = Label(RootFXMenu, text="a:",font=500)
    method_label.grid(row=2,column=0,pady=10)
    method_Enter2=Entry(RootFXMenu,textvariable="")
    method_Enter2.grid(row=2,column=1,pady=10)

    method_label = Label(RootFXMenu, text="b:",font=500)
    method_label.grid(row=3,column=0,pady=10)
    method_Enter3=Entry(RootFXMenu,textvariable="")
    method_Enter3.grid(row=3,column=1,pady=10)

    method_label = Label(RootFXMenu, text="y0:",font=500)
    method_label.grid(row=4,column=0,pady=10)
    method_Enter4=Entry(RootFXMenu,textvariable="")
    method_Enter4.grid(row=4,column=1,pady=10)

    method_label = Label(RootFXMenu, text="k:",font=500)
    method_label.grid(row=5,column=0,pady=10)
    method_Enter5=Entry(RootFXMenu,textvariable="")
    method_Enter5.grid(row=5,column=1,pady=10)

    method_Enter=Button(RootFXMenu,text="calculate",command=lambda:CalculateSystem(method_Enter1.get(),float(method_Enter2.get()),float(method_Enter3.get()),float(method_Enter4.get()),int(method_Enter5.get()),method))
    method_Enter.grid(row=6,column=1)

    return RootFXMenu

def LoadMenu(opened,method=0):
    global activeMenu
    activeMenu.destroy()

    if(opened==0):
        activeMenu = SpawnMainMenu()
    elif(opened==1):
        activeMenu = SpawnRootFXMenu(method)
    elif(opened==2):
        activeMenu = SpawnIntegFXMenu(method)
    elif(opened==3):
        activeMenu = SpawnSystemFXMenu(method)

def DoMethod(y,rot):
    global method_label1
    method_label1.destroy()
    method_label1 = Label(rot, text=y,font=500)
    method_label1.grid(row=0,column=1,pady=25)

root = Tk()
root.title("Уравнения")
activeMenu=SpawnMainMenu()
method_label1=Label()

root.mainloop()


