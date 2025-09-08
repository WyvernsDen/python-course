value = 0
frange = int(input("Type in the range for the Fibonacci sequence: "))
x = 0
y = 1
sequence = "0, 1"
while value < frange:
    value = x + y
    if value < frange:
        x = y
        y = value
        sequence += ", " + str(value)
print(f"Fibonacci: {sequence}")
