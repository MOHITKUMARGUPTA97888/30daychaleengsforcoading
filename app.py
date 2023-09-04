
'''

'''

W=["mohita","bke","mohit","ROHIT","dgfo","jfcu","asfe"]
count=0
for j in W:
    c=j.lower()
    b=c[-1]
    # print(b)
    if (b[0]== "a" or b[0]== "e" or b[0]== "i" or b[0]== "o" or b[0]== "u"):
        count+=1
print(count)

# ch = input()
# if(ord(ch) >= 65 and ord(ch) <= 90):
#     print("upper")
# elif(ord(ch) >= 97 and ord(ch) <= 122):
# 	print("lower")
# elif(ord(ch) >= 48 and ord(ch) <= 57):
# 	print("Number")
# else:
# 	print("Symbol")
# aray=["civic", "radar", "level", "rotor", "kayak", "madam"]
# for i in aray:
#     if i[::-1]==i:
#         print("ist paradrome")
# a=[9,-9,8,6,5,-15,-36,36,6,-8,-3,-7,144]
# count=0
# for i in a:
#     b=i**0.5
#     if b*b==i:
#         count+=1
# print(count)   
# print(a)
# print(2197**ug)