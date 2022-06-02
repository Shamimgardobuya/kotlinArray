import random
people_Think=random.sample(range(0,100),100)
z=[]
# i=2
for i in people_Think:
    print(people_Think[0])
def average():
    x = []
    while len(x)!=10:
        user = int(input("enter 10 elements"))
        x.append(user)
        y = len(x)
        total = sum(x)
    aver= total/y
    print(aver)   


average()
     