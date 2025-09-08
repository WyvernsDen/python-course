numerator = int(input("Type the numerator in: "))
exponent = int(input("Type the exponent in: "))
result = 0

for i in range(exponent):
    if i < exponent:
        i += i
        result = numerator * numerator
    if i == exponent:
        print(f"{numerator}^{exponent} = {result}")
        break