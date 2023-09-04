def is_prime(n):
    if n<=1:
        return False
    for i in range(2 ,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def main():
    for i in range(2,100):
        if is_prime(i):
            print(i,end=" ")

if __name__=="__main__":
    main()