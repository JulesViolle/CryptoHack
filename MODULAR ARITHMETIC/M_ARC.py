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
