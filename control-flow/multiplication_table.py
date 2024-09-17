num = int(input("Enter a number to see its multiplication table: "))

for i in range(1,11):
    result = num * i
    print(f"{num} * {i} = {result}")