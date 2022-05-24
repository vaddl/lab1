#5
a=int(input('vvedit chislo:'))
b=int(input('vvedit chislo:'))
c=int(input('vvedit chislo:'))
if a and b and c >0:
    g=(a*b*c/3)
    print(g)
else:
    print('error')

    #10
a=int(input('vvedit kilkist baita: '))
print('kilkist kilobaitiv: ',a//1024)


#11

x = int(input('vvedit x: '))
y = 3*pow(x,6)+6*pow(x,2)+7
print('znachennya F',y)


#12
a=float(input('vvedik kyt:' ))
if a>=0 and a<360:
    r=a/180*3.14
    print(r)
else:
    print('error')
        
    
#13
x1 = float(input("x1"))
y1 = float(input("y1"))
x2 = float(input("x2"))
y2 = float(input("y2"))
u = abs(x2-x1)
l = abs(y2-y1)
p = 2*(u+l)
S=u*l
print("perymtr:",p,",","ploscha:",S)
