def operation_input():
  print("Enter the desired operation symbol or it's numeric value: ")
  print("1: + (addition)")
  print("2: - (subtraction)")
  print("3: * (multiplication)")
  print("4: / (division)")
  return input()


num1 = float(input("Enter the first number: "))
operation = operation_input()
num2 = float(input("Enter the second number: "))

if operation == "+" or operation == "1":
  result = num1 + num2
elif operation == "-" or operation == "2":
  result = num1 - num2
elif operation == "*" or operation == "3":
  result = num1 * num2
elif operation == "/" or operation == "4":
  if num2 == 0:
    print("Error: Division by zero")
    exit()
  else:
    result = num1 / num2
else:
  print("Invalid operation")

if result % 1 == 0:
  result = int(result)

print(f"The result is {result}")

