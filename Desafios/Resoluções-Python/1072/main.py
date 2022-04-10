n = int(input())
value_in = 0
value_out = 0

for i in range(n):
    value = int(input())
    if 10 <= value <= 20:
        value_in += 1
    else:
        value_out += 1

print(value_in,"in")
print(value_out,"out")
