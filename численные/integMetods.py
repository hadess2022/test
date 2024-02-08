
def CalculateInteg(yr,a,b,k,e,i):
    if(i==0):
        return IntegSquare(yr,a,b,k,e)
    elif(i==1):
        return IntegTrap(yr,a,b,k,e)
    elif(i==2):
        return IntegSims(yr,a,b,k,e)

maxI=10

def IntegSquare(yr,a,b,k,e):
    for i in range(maxI):
        dx=(b-a)/k
        ax=a+dx/2
        sum=0
        for j in range(k):
            sum+=f(ax+j*dx,yr)
        s=0
        for j in range(k):
            s+=f(ax+j*dx,yr)
        
        if(abs(s-sum)*dx<e):
            return "достигнута нужная точность: "+str(s*dx)
        
        k*=10

    return "достигнут предел выполнения: "+str(s*((b-a)/k))

def IntegTrap(yr,a,b,k,e):
    for i in range(maxI):
        dx=(b-a)/k
        sum=0
        for j in range(k):
            sum+=(f(a+j*dx,yr)+f(a+(j+1)*dx,yr))/2
        s=0
        for j in range(k):
            s+=(f(a+j*dx,yr)+f(a+(j+1)*dx,yr))/2
        
        if(abs(s-sum)*dx<e):
            return "достигнута нужная точность: "+str(s*dx)
        
        k*=10

    return "достигнут предел выполнения: "+str(s*((b-a)/k))

def IntegSims(yr,a,b,k,e):
    for i in range(maxI):
        dx=(b-a)/k
        sum=0
        for j in range(k):
            sum+=(f(a+j*dx,yr)+4*f(a+j*dx+dx/2,yr)+f(a+(j+1)*dx,yr))*dx/6
        
        k*=10
        dx=(b-a)/k

        s=0    
        for j in range(k):
            s+=(f(a+j*dx,yr)+4*f(a+j*dx+dx/2,yr)+f(a+(j+1)*dx,yr))*dx/6

        if(abs(s-sum)*dx<e):
            return "достигнута нужная точность: "+str(s*dx)
        
        k*=10

    return "достигнут предел выполнения: "+str(s*((b-a)/k))


def f(x,yr):
    return eval(yr)