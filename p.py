# # import requests
# # import os
# # from requests.cookies import RequestsCookieJar
# # from http.cookiejar import CookieJar
# # # Get the username and password for the Instagram account.
# # username = "oggy_adinath"
# # password = "QWErty9420408659@#$04"

# import instaloader

# loader = instaloader.Instaloader()
# loader.load_session_from_file("oggy_adinath", "C:/Users/91724/AppData/Local/Instaloader/session-oggy_adinath")

# # # Use the loader object for various interactions with Instagram
# profile = instaloader.Profile.from_username(loader.context, "janhavi.bajpai")
# # profile.get_posts()

# # Access the profile picture URL
# profile_pic_url = profile.profile_pic_url

# # Print the profile picture URL
# a=10
# # v=10
# # print(f"{a+v}\n")
# # print(f"{a*v}\n")     
# a=2100
# b=a//4
# c=a/4
# if b==c:
#     print("True leep")
#     print(b)
#     print(c)
# else:
#     print("False")
#     print(b)
#     print(c)
# print(range(0,5))
# def lis_compesist(x,y,z,n):
#     lis=[]
    
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 list1=[i,j,k]
#                 lis.append(list1)
#     return lis
# x = 1
# y = 1
# z = 1
# n = 2
# print(lis_compesist(x,y,z,n))
# # Generate all permutations of [i, j, k]
# permutations = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

# # Filter elements whose sum is not equal to n
# filtered_permutations = [perm for perm in permutations if sum(perm) != n]

# # Print the filtered array
# print(filtered_permutations)

# if __name__ == '__main__':
#     n = 5
#     arr = [2, 3, 6, 6, 5]
#     # N=0
    # M=0
    # list=[]
    # for i in arr :
    #     if i>N:
    #         N=i
    # for i in arr:
    #     if N != i:
    #         list.append(i)
    # for i in list :
    #     if i>M:
    #         M=i
    # print(M)

    # arrs = set(arr) 
    # ans = list(sorted(arrs,reverse=True)) 
    # print(ans[1])
# if __name__ == '__main__':
#     list=[]
#     b=[]
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
        
#         b.append(score)
#         list.append([name,score])
#     # b.sort()
#     a=list(set(b))
#     c=a[1]
#     list.sort()
#     for i in  list:
#         if i[1]==c:
#             print(i[0]) 
# N=input()
# K=int(input())
# arr=[1,23,12,9,30,2,50]
# print(arr[::-1])
# b=list(arr)
# b.sort()
# b.reverse()
# for i in range(K):
#     print(b[i],end= "")
# def funn(a, b):
#     if ((b - a) < (a | b) and a > 4):
#         b = (b + 1) + b
#         a = 3 + 1 + a
#         return funn(a, b + a) + a + funn(a, b)
#     else:
#         a = 1 + a + a
#         return a - b + 1
# funn(8,9)
###3====================######## input in dict
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for i in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
   
#     a=0
#     for j in (student_marks[query_name]):
       
#         a=j+a
#     print(a/len(student_marks[query_name]))
############===========================##################
def find(l):
    
    for i in l:
        if i==2000:
            print(i)
expense={"January" : 2200,"February" : 2350
,"March" : 2600
,'April' : 2130
,'May'  :2190}
print(expense["February"]-expense["January"])
print(expense["February"]+expense["January"]+expense["March"])
expense["June"]=1980
find(expense.values())


# dict(5)
# January 2200
# February 2350
# March  2600
# April  2130
# May  2190
# print(expense["February"]-expense["January"])
######################+===========================================####################
# import time
# import datetime
# print(datetime.datetime.now())
# import pytz
# date=datetime.date.today()
# print(date)
# print(time.strftime("%H:%M:%S",time.localtime()))
