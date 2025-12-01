a = 3.0
b = 5.0
w1 = 2.0
w2 = 1.5
bias = 1.0
s1 = 0.0
tw = 0.0
norm = 0.0
final_score = 0.0
###Code###
s1 = a * w1 + b * w2
tw = w1 + w2
norm = (lambda: s1 / tw)()
final_score = norm ** 2 if a < b else (norm - bias) ** 2
#Result:final_score
#Name:weighted_mean_score #Desc:Computes obfuscated weighted mean, applies nonlinear squaring and bias conditional using lambdas and intermediate variables only
