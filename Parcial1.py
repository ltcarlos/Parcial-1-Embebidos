from machine import mem32
import uctypes
import array

def Bezier(n,PO,P1,P2,P3):
    LR=[]
    n1=n+1
    for i in range(n1):
        t=i/n
        t3=(1-t)*(1-t)*(1-t)
        t2=(1-t)*(1-t)
        t1=(1-t)
        dir_PO=uctypes.addressof(PO)
        dir_P1=uctypes.addressof(P1)
        dir_P2=uctypes.addressof(P2)
        dir_P3=uctypes.addressof(P3)
        LRN=[]
        for j in range(len(PO)):
            C1=t3*mem32[dir_PO+4*j]
            C2=3*t2*mem32[dir_P1+4*j]*t
            C3=3*t*t*t1*mem32[dir_P2+4*j]
            C4=t*t*t*mem32[dir_P3+4*j]
            CT=C1+C2+C3+C4
            LRN.append(CT)
        LR.append(LRN)
    return(LR)

n=3
PO = array.array('i', [0, 0])
P1 = array.array('i', [1000, 0])
P2 = array.array('i', [1000, 1000])
P3 = array.array('i', [0, 1000])
print(Bezier(n,PO,P1,P2,P3))
        
    

