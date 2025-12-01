a = 3
b = 5.0
w1 = 2
w2 = 3
offset = 1.5
inter1 = 0
inter2 = 0
denom = 1
score = None
###Code###
inter1 = a * w1
inter2 = b * w2
denom = w1 + w2
score = (lambda: (inter1 + inter2) / denom + offset)() if denom != 0 else offset
#Result:score
#Name:weighted_mean_score
#Desc:Computes obfuscated weighted average using intermediate variables, lambda call, and conditional fallback for zero denominator handling