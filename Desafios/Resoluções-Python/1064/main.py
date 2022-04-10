list_values = []
value_positives = 0
media = 0

for i in range(6):
    list_values.append(float(input()))

for value in list_values:
    if value > 0:
        value_positives += 1
        media += value

print(f'{value_positives} valores positivos')
print(round((media/value_positives),1))
