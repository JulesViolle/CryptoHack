def stGCD(n,w):
    a,b=1,0
    c,d=0,1
    s,t=0,0
    r=n%w
    
    while [r:=n%w]!=[0]:
        g=n//w
        s,t = a-g*c,b-g*d
        
        a,b,c,d=c,d,s,t

        n=w
        w=r
    return (s,t)
        
print(stGCD(26,23))

OR

def SecendGCD(n,w):
    s=pow(n,-1,w)
    t=(1-(n*s))/w
    return (s,t)
print(SecendGCD(26,23))


