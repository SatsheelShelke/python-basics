speeds=[100,120,85,70,115]
for i in speeds:
    print(i)

speeds.sort()
print("Max Speed=",speeds[-1])
print("min speed=",speeds[0])

total=0
for i in speeds:
    if i>0:
        total+=i
print('total=',total)
avg=total/len(speeds)
print(avg)

abv100=[]
for i in speeds:
    if i>100:
        abv100.append(i)

print(abv100)
