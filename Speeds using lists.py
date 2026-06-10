#List
speeds = [100,120,85,70,115]

#Print all Lists
for i in speeds:
    print(i)

#Calculate total & average
total=0
for i in speeds:
        total+=i

print('total=',total)
avg=total/len(speeds)

print('Average=',avg)
#Max and Min speeds
largest=speeds[0]
smallest=speeds[0]
for i in speeds:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i

print('Max Speed=',largest)
print('Min Speed='smallest)

#above 100 speed
above_100_speeds=[]
for i in speeds:
    if i>100:
        above_100_speeds.append(i)

print('Above 100 speed',above_100_speeds)
