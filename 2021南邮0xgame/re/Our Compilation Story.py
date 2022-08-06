# from flag import flag
# str= "qwq"
# len_flag=len(flag)
# for i in range(len_flag):
#     i=chr(ord(str[i]) ^ ord(flag[i]))
#     str= str + i
#
# str= str[::-1]
# len_flag= len(str) - 1
# for i in range(len_flag):
#     print(ord(str[i]), end=",")
# print(ord(str[len_flag]))
#21,44,45,104,31,30,26,121,65,125,23,112,77,46,47,126,89,112,7,109,7,88,10,105,104,59,54,91,83,98,32,54,15,65,113,119,113

str = [21,44,45,104,31,30,26,121,65,125,23,112,77,46,47,126,89,112,7,109,7,88,10,105,104,59,54,91,83,98,32,54,15,65,113,119,113]
str = str[::-1]
len_flag = len(str) + 1
str1 = str[3:]
flag = [0]*99
for i in range(len(str1)):
    flag[i] = str[i] ^ str1[i]

print(bytes(flag).decode())

