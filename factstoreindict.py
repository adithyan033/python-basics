
dictt={}

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
n1=int(input("enter the starting range "))
n2=int(input("enter the ending range"))
    
for num in range(n1,n2):
    dictt[num]=fact(num)
    
    
print(dictt)