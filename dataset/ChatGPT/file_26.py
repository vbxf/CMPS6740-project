a = 4
b = 7.5
c = 2
w1 = 1
w2 = 2
w3 = 3
scale = 1.2
temp = 0
threshold = 5
###Code###
x1 = a * w1
x2 = b * w2
total = x1 + x2 + c * w3
score = (total / (w1 + w2 + w3)) if total != 0 else 0
final = (lambda: score * scale)()
#Result:final
#Name:obfuscated_weighted_mean
#Desc:Computes obfuscated weighted mean using lambdas and conditional fallback with redundant intermediate variables for extra robustness