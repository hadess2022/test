
def CalculateRoot(yr,a,b,e,i):
    if(i==0):
        return HalfRoot(yr,a,b,e)
    elif(i==1):
        return HordRoof(yr,a,b,e)
    elif(i==2):
        return TangentRoof(yr,a,b,e)
    elif(i==3):
        return HordAndTangentRoof(yr,a,b,e)

maxI=10000

def HalfRoot(yr,a,b,e):
    if(f(a,yr)/abs(f(a,yr))==f(b,yr)/abs(f(b,yr))):
        return "не возможго найти корень по этому методу"

    for i in range(maxI):
        x=(a+b)/2

        if(f(x,yr)==0):
            return "корень найден: "+ str(x)

        if(abs(f(a,yr)-f(b,yr))<e):
            return "достигнута нужная точность корня: "+str((a+b)/2)

        if(f(x,yr)/abs(f(x,yr))==f(b,yr)/abs(f(b,yr))):
            b=x
        else:
            a=x
    
    return "достигнут предел вычислений: "+str((a-b)/2)


def HordRoof(yr,a,b,e):
    if(f(a,yr)/abs(f(a,yr))==f(b,yr)/abs(f(b,yr))):
        return "не возможго найти корень по этому методу"

    for i in range(maxI):
        f1=f(a,yr)*(b-a)
        f2=f(b,yr)-f(a,yr)
        x=a-(f1/f2)

        if(f(x,yr)==0):
            return "корень найден: "+ str(x)

        if(f(a,yr)-f(b,yr)<e):
            return "достигнута нужная точность корня: "+str((a+b)/2)

        if(f(x,yr)/abs(f(x,yr))==f(b,yr)/abs(f(b,yr))):
            b=x
        else:
            a=x
    
    return "достигнут предел вычислений: "+str((a-b)/2)


def TangentRoof(yr,a,b,e):
    if(f(a,yr)/abs(f(a,yr))==f(b,yr)/abs(f(b,yr))):
        return "не возможго найти корень по этому методу"

    x01=f0(a+e,yr,e)
    x02=f0(a-e,yr,e)
    x00=(x01-x02)/(2*e)
    side=f(a,yr)*x00<0

    if(side):
        x=b
    else:
        x=a

    for i in range(maxI):
        x=x-(f(x,yr)/f0(x,yr,e))

        if(f(x,yr)==0):
            return "корень найден: "+ str(x)

        if(side):
            if(abs(f(x,yr)-f(x-e,yr))<0):
                return "достигнута нужная точность корня: "+str(x)
            b=x
        else:
            if(abs(f(x,yr)-f(x+e,yr))<0):
                return "достигнута нужная точность корня: "+str(x)
            a=x
    
    return "достигнут предел вычислений: "+str(x)


def HordAndTangentRoof(yr,a,b,e):
    if(f(a,yr)/abs(f(a,yr))==f(b,yr)/abs(f(b,yr))):
        return "не возможго найти корень по этому методу"

    x01=f0(a+e,yr,e)
    x02=f0(a-e,yr,e)
    x00=(x01-x02)/(2*e)
    side=f(a,yr)*x00<0

    for i in range(maxI):
        f1=f(a,yr)*(b-a)
        f2=f(b,yr)-f(a,yr)
        x=a-(f1/f2)

        if(f(x,yr)==0):
            return "корень найден: "+ str(x)

        if(f(a,yr)-f(b,yr)<e):
            return "достигнута нужная точность корня: "+str((a+b)/2)

        if(abs(f(a,yr)*f(x,yr))<0):
            b=x
            a=a-(f(a,yr)/f0(a,yr,e))
        else:
            a=x
            b=b-(f(b,yr)/f0(b,yr,e))

    return "достигнут предел вычислений: "+str((a-b)/2)





def f(x,yr):
    return eval(yr)

def f0(a,yr,e):
    return (f(a+e,yr)-f(a-e,yr))/(2*e)
