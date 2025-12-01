p = 6
q = 4
r = 10
alpha = 0.5
beta = 1.2
gamma = 0.8
temp1 = 0.0
temp2 = 0.0
adjusted = 0.0
final_output = 0.0
###Code###
temp1 = (lambda: p * alpha + q * beta)()
temp2 = (lambda: r * gamma)()
adjusted = temp1 + temp2
final_output = adjusted / r if adjusted > r else adjusted * alpha
#Result:final_output
#Name:weighted_adjusted_ratio
#Desc:Calculates weighted ratio with lambda-based combination and conditional scaling using simple arithmetic and obfuscated constants