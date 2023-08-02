import sys
import matplotlib.pyplot as plt
import numpy as np  
import re

class Calculator:
   
   def add(self, a, b):
      return a + b
    
   def subtract(self, a, b):
      return abs(a - b)
    
   def multiply(self, a, b):
      return a * b
    
   def divide(self, a, b):
      if b != 0:
         return a/b
      else:
         print("Division not possible!")
   
   def quadratic():
      function = str(input("Usage: python caculator.py <aX^2 + bX + C>"))
      terms = re.split(r'[+-]', function)
      x = np.arange(-10, 10, 1)
   
   def evalTerm(self, term, x_val):
      x_sub_term = term.replace("X", str(x_val))
      return eval(x_sub_term)
   
print("Usage: python calculator.py <operation> <a> <b>")
print("Available operations: add, subtract, multiply, divide")
option = str(input("[1]: Arithmetic [2]: Graph [3]: Matrix"))

if __name__ == "__main__":

   calculator = Calculator()

   if option == "1":
      while True:
         try: 
            operation = sys.argv[1].lower()
            a = float(sys.argv[2])
            b = float(sys.argv[3])

            calculator = Calculator()

            if operation == "add":
               result = calculator.add(a, b)
                  
            elif operation == "subtract":
               result = calculator.subtract(a, b)

            elif operation == "multiply":
               result = calculator.multiply(a, b)
                  
            elif operation == "divide":
               result = calculator.divide(a, b)
                  
            else:
               print("Invalid input; Usage: python calculator.py <operation> <a> <b>")
                  
            print("Result: ", result)
            break

         except ValueError:
            print("Invalid input; Usage: python calculator.py <operation> <a> <b>")
   
   elif option == "2":
      while True:   
         try:
            x_values = []
            y_values = []
      
            function = str(input("Usage: <a * X^2 + b * X + C>: "))
            function = function.replace("^2", "*X")
            for x in range(-10,10):
               x_values.append(x)
               y = calculator.evalTerm(function, x)
               y_values.append(y)

            plt.plot(x_values, y_values)

            plt.title(f"Quadratic equation: {function}")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")

            plt.show()
            break

         except ValueError:
            print("Invalid input! Usage: <a * X^2 + b * X + C>: ")
