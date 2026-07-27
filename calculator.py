num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

print("----- CALCULATOR RESULTS -----")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")

if num2 == 0:
    print(f"{num1} / {num2} = Error: Cannot divide by zero!")
    print(f"{num1} // {num2} = Error: Cannot divide by zero!")
    print(f"{num1} % {num2} = Error: Cannot divide by zero!")
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"{num1} / {num2} = {division}")
    print(f"{num1} // {num2} = {floor_division}")
    print(f"{num1} % {num2} = {modulus}")

print("-------------------------------")
