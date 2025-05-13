import random
n=random.randint(1,100)
a=-1
guess=0
while(n!=a):
    guess +=1
    a=int(input("guess the number"))
    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")
    
print(f"your choose right number {a}, {guess} ateemps")