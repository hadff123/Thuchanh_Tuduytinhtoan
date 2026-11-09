def tri(a,b,c):
    if(a>0 and b>0 and c>0 and a+b>c and b+c>a and c+a>b):
        return True
x,y,z = map(float,input().split())
if (tri(x,y,z) == True):
    if(x==y or y==z or z==x):
        if(x==y and y==z):
            print("Tam giac deu")
        elif(x**2+y**2==z**2 or y**2+z**2==x**2 or z**2+x**2==y**2):
            print("Ttam giac vuong can")
        else:
            print("Tam giac can")
    else:
        if(x**2+y**2==z**2 or y**2+z**2==x**2 or z**2+x**2==y**2):
            print("Tam giac vuong")
        else:
            print("Tam giac thuong")
else:
    print("Khong la ba canh cua mot tam giac")
p=(x+y+z)/2
dien_tich=(p*(p-x)*(p-y)*(p-z))**0.5
print("Chu vi:", p*2)
print("Dien tich:",dien_tich)