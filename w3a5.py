a,b,c = map(float,input().split())
if (a == 0):
    
    if(b==0):
        if(c==0):
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem duy nhat la",-c/b)
else:
    denta = b**2 - 4*a*c
    if(denta < 0):
        print("Phuong trinh vo nghiem")
    elif(denta == 0):
        print("Phuong trinh co nghiem kep",-b/(2*a))
    else:
        print("Phuong trinh co 2 nghiem phan biet la",(-b+denta**0.5)/(2*a),"va",((-b-denta**0.5)/(2*a)))



