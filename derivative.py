import sympy

# Define the variable x
x = sympy.Symbol('x')

# Define the function f(x)
expr = input("Enter the function f(x): ")
f = sympy.sympify(expr)

# Calculate the derivative of f(x)
df = sympy.diff(f, x)

# Print the result
print("The derivative of f(x) =", df)
