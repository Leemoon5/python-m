tem_str = input("please input temperature(F or C)")
unit = tem_str[-1] # The unit of tem
num = float(tem_str[0:-1])
if unit in ['C', 'c']:
    mun_F = num*1.8+32
    print("Converted Fa... is {}F".format(mun_F))
elif unit in ['F', 'f']:
    mun_C = (num-32)/1.8
    print("Converted Celsius is {}C".format(mun_C))
else:
    print("It's a wrongly input")
