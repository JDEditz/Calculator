def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y == 0:
       raise ValueError("Cannot divide by zero")
   return x / y

def power(x, y):
   return x ** y

def square_root(x):
   if x < 0:
       raise ValueError("Cannot find the square root of a negative number")
   return x ** 0.5

print("Welcome To The Calculator")
print("")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("")

while True:
   choice = input("Enter choice (1/2/3/4/5/6): ")

   if choice in ('1', '2', '3', '4', '5', '6'):
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))

       if choice == '1':
           print(num1, "+", num2, "=", add(num1, num2))

       elif choice == '2':
           print(num1, "-", num2, "=", subtract(num1, num2))

       elif choice == '3':
           print(num1, "*", num2, "=", multiply(num1, num2))

       elif choice == '4':
           try:
               print(num1, "/", num2, "=", divide(num1, num2))
           except ValueError as e:
               print(e)

       elif choice == '5':
           print(num1, "raised to the power", num2, "=", power(num1, num2))

       elif choice == '6':
           try:
               print("Square root of", num1, "=", square_root(num1))
           except ValueError as e:
               print(e)

       break
   else:
       print("Invalid Input")