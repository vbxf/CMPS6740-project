p = 6
q = 4
r = 10
alpha = 0.6
beta = 0.4
temp1 = 0.0
temp2 = 0.0
weighted_sum = 0.0
adjusted = 0.0
result = 0.0
###Code###
temp1 = (lambda: p * alpha + q * beta)()
temp2 = (lambda: r * beta)()
weighted_sum = temp1 + temp2
adjusted = weighted_sum / (p + q) if p > q else weighted_sum / (q + r)
result = adjusted * 2.0
#Result:result
#Name:adaptive_weighted_average
#Desc:Calculates adaptive weighted average using lambdas and conditional divisor based on relative variable magnitudes only
