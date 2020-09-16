'''
三次方格式化
获得用户输入的一个数字，可能是整数或浮点数，a，计算a的三次方值，并打印输出。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬
输出结果采用宽度20个字符、居中输出、多余字符采用减号(-)填充。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬
如果结果超过20个字符，则以结果宽度为准。
示例 1	
10
--------1000--------
'''
import re
s = input()

# s_sp = s.split(".")
# print(s_sp)
print(re.findall('^0$|^[1-9]\d*$', s))

# for i in range(len(s_sp)):
#     if re.findall("\d", s_sp[0]):


# pr
# # print(re.findall("(\d.*?).(\d.*?)", s))
# re.findall("\.?", s) 
# def num():
#     for i in s:

# a = float(s)
# a = a**3
# print(a)


# import re 
# s=input()
# if s.count('.')==1:
#     if re.match('(\d.*?).(\d.*?)',s) != None:
#         s=float(s)
#         result=s**3
#     else:
#         print("it's a ")
# print(result)
# print(re.match==('(\d.*?).(\d.*?)',s))