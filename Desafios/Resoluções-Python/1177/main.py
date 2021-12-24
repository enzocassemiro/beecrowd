v = int(input())
y = 0
for x in range(1000):
    print(f"N[{x}] = {y}")
    if y != v-1:
        y+=1
    else:
        y=0
