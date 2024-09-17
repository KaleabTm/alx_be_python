num = int(input ("Enter a number to see its multiplication table: "))

for i in range(1,11):
    value=num * i
    print(f"{num} * {i} = {value}")