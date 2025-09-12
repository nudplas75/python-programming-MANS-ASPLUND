import math

TP = 2
FP = 2
FN = 11
TN = 985

accuracy = (TP + TN) / (TP + TN + FP + FN)

print(f" {accuracy:.3f}")

# This is a good model mathematically, but statistical answers
# where the outcome is below 1% give the person interpreting the
# answer very little information. I had chosen a graphical presentation
# wich, despite the low precentage, would have given an answer that
# is easier to interpret
