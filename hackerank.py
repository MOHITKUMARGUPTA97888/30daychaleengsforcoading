# Enter your code here. Read input from STDIN. Print output to STDOUT4
n=int(input())
for i in range(n):
    print(" "*(n-i)+"H"*(2*i+1))
for i in range (n+1):
    print(" "*(n//2)+"H"*(n)+" "*((2*n-1)+6)+"H"*(n))
for i in range(n//2+1):
    print(" "*(2)+"H"*(n*5))
for i in range (n+1):
    print(" "*(n//2)+"H"*(n)+" "*((2*n-1)+6)+"H"*(n))
j=n
for i in range(n):
    print(" "*(n*n),end=" ")
    print(" "*(i+2)+"H"*(2*j-1))
    j-=1


thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

