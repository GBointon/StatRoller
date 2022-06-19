import random
for stat in range(1,7):
    stat_range=random.sample(range(1,7),4)
    stat_range.sort()
    del stat_range[0]
    sum=0
    for n in stat_range:
        sum+=n
    print(sum)