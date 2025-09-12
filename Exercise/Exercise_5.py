import math

# givna punkter
x1, y1 = 4, 4
x2, y2 = 0, 1

# uträkning lutning
k = (y2 - y1) / (x2 - x1)

# skärpunkt
m = y1 - k * x1

# printa svaret
print(f"vinkel {k}")
print(f"skärpunkt {m}")
print(f"linjens ekvation y = {k}x + {m}")
