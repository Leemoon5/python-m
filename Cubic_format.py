# 三次方格式化
import re
def len20(str_a):
    str_a = str(a)
    if len(str_a) < 20:
        return "{:-^20}".format(a)
    else:
        return a

s =input()

if re.findall('^0$|^[1-9]\d*$', s) != []:
    a = int(s)
    a = a**3
    print(len20(a))
elif re.findall('^0\.\d+$|^[1-9]\d*\.\d+$', s) != []:
    a = float(s)
    a = a**3
    print(len20(a))
else:
    print("It's a wrong input")







