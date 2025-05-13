import random
n=random.randint(1,100)
a=-1
guess=1
while(n!=a):
    a=int(input("guess the number"))
    if(a>n):
        print("Lower number please")
        guess +=1
    elif(a<n):
        print("Higher number please")
        guess +=1
    
print(f"your choose right number {a}, {guess} attempts")