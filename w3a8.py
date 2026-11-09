a,b,m,c,d,n = map(float, input().split())
D=a*d-b*c
Dx=m*d-b*n
Dy=a*n-m*c
if(D != 0):
    x=Dx/D
    y=Dy/D
    print("He phuong trinh co nghiem la",x,"va",y)
else:
    if(Dx ==0 and Dy == 0):
        print("He phuong trinh co vo so nghiem")
    else:
        print("He phuong trinh vo nghiem")
        