import math

x1, y1 = 4, 4
x2, y2 = 0, 1

k = (y2 - y1) / (x2 - x1)

m = y1 - k * x1

print(f"vinkel {k}")
print(f"skärpunkt {m}")
print(f"linjens ekvation y = {k}x + {m}")
