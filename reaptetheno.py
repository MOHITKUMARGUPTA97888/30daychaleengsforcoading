'''Repeat the characters
Create a Python function that accepts a string.
The function should return a string, with each character in the original string doubled.
If you send the function “now” as a parameter, 
it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.'''

def reapet(arg):
    
    for i in arg:
        a=i*2
        print(a,end="")

   
if __name__=="__main__":
    reapet("sorry6582")
