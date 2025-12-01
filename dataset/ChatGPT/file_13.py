a = 4
b = 7
c = 2
w1 = 0.5
w2 = 0.3
w3 = 0.2
bias = 1
threshold = 5
temp = None
###Code###
sum_w = (lambda: w1 + w2 + w3)()
weighted = (lambda: a * w1 + b * w2 + c * w3)()
norm = weighted / sum_w
final = norm + bias if norm > threshold else norm - bias
#Result:final
#Name:weighted_mean_score #Desc:Computes obfuscated weighted mean using lambdas, intermediate variables, conditional adjustment, normalization, and additive bias correction step