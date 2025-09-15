import math

TP = 2
FP = 2
FN = 11
TN = 985

accuracy = (TP + TN) / (TP + TN + FP + FN)

print(f" {accuracy:.3f}")

# Det beror på i vilken situation det gäller.
