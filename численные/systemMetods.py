import matplotlib.pyplot as plt
from tkinter import *

def CalculateSystem(yr1,a,b,y0,k,i):
    if(i==0):
       Eyler(yr1,a,b,y0,k)
    elif(i==1):
       Rynge_Kyt(yr1,a,b,y0,k)

def Eyler(yr1,a,b,y0,k):
    h=((b-a)/k)
    x=a
    y1=[f(x,y0,yr1)]
    for i in range(k):
        dy1=f(x,y1[i],yr1)*h
        y1.append(y1[i]+dy1)
        x+=h



    plt.close()
    t=[a+h*i for i in range(len(y1))]
    plt.plot(t,y1,'g-')
    plt.legend([str(yr1)], loc=2)
    plt.show()


def Rynge_Kyt(yr1,a,b,y0,k):
    global root
    h=((b-a)/k)
    x=a
    y1=[f(x,y0,yr1)]
    for i in range(k-1):

        ky11=y1[i]*h

        ky12=f(x+h/2,y1[i]+ky11/2,yr1)*h

        ky13=f(x+h/2,y1[i]+ky12/2,yr1)*h

        ky14=f(x+h/2,y1[i]+ky13,yr1)*h

        dy1=(ky11+2*ky12+2*ky13+ky14)/6

        y1.append(y1[i]+dy1)
        x+=h

    plt.close()
    t=[a+h*i for i in range(len(y1))]
    plt.plot(t,y1,'g-')
    plt.legend([str(yr1)], loc=2)
    plt.show()




def f(x,y,yr):
    return float(str(eval(yr))[:10])