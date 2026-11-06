name = input("Ten chu ho:" )
pre_elec_val = float( input("Chi so thang truoc: "))
now_elec_val = float( input("Chi so thang nay: "))
elec_val = now_elec_val - pre_elec_val
money = 0
if(elec_val <=50):
    money = elec_val*1984
elif(elec_val <= 100):
    money= 50*1984+(elec_val-50)*2050
elif(elec_val <= 200):
    money= 50*1984 + 50*2050 + (elec_val - 100)*2380
elif(elec_val <= 300):
    money = 50*1984 + 50*2050 + 100*2380 + (elec_val-200)*2998
elif(elec_val <= 400):
    money = 50*1984 + 50*2050 + 100*2380 + 100*2998+(elec_val-300)*3350
else:
    money = 50*1984 + 50*2050 + 100*2380 + 100*2998+100*3350+(elec_val-400)*3460
total_money = round(money*1.08)
print("Ho va ten: ",name)
print("Tien phai tra la: ",total_money)
