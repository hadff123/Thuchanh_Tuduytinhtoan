a,b = map(float,input().split())
if(a==0):
    if(b==0):
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    print("Phuong trinh co nghiem duy nhat la",-b/a)


