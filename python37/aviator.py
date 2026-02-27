import random
a=random.uniform(1,100)

for i in range(1,1000):
    print(i*0.01)
    if a == i:
        break
print(a)
