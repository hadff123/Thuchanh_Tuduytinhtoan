a,b,c = map(float,input().split())
max_val = max(a,b,c)
max_val = c
p = (a+b+c)/2
if(a>0 and b>0 and c>0 and a+b > c):
    square = (p*(p-a)*(p-b)*(p-c))**0.5
    print(f"{square:.1f}")
else:
    print("Khong phai 3 canh cua tam giac")
