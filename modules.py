import os
import math

# 1
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# 2
num = int(input("Enter an integer: "))
log_val = math.log2(num)
print(f"Log base 2 of {num} is: {log_val}")

# 3
print(f"Floor: {math.floor(log_val)}")
print(f"Ceiling: {math.ceil(log_val)}")