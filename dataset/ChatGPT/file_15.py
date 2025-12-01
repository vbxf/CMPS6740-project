a = 7
b = 3.5
c = 2
w1 = 0.6
w2 = 0.3
w3 = 0.1
scale = 10.0
thr = 5
bias = 1.2
tmp = None
###Code###
weighted = a*w1 + b*w2 + c*w3
den = (w1 + w2 + w3)
norm = (lambda: (weighted/den) * scale + bias)()
final_score = norm if den > 0 else 0
#Result:final_score
#Name:weighted_normalized_score
#Desc:Computes obfuscated normalized weighted score using lambdas, intermediate variables, conditional fallback when denominator nonpositive and bias
