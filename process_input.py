#!/usr/bin/env python3
import sys

# Retrieve command-line arguments and convert them to integers
x, y, z = map(int, sys.argv[1:4])

print("<h2>Step-by-step Calculation</h2>")

# Perform shortcut operator operations and display intermediate steps
x += y
print(f"x += y → {x}<br>")

x -= z
print(f"x -= z → {x}<br>")

x *= y
print(f"x *= y → {x}<br>")

x %= z
print(f"x %= z → {x}<br>")

# Division only if z is not zero
if z != 0:
    x /= z
    print(f"x /= z → {x}<br>")

# Final result is sum of updated x, y, and z
result = x + y + z
print(f"<h3>Final Result: {result}</h3>")
