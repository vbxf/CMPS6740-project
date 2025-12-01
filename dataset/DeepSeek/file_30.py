p = 8
q = 16
r = 6
s = 2
boundary = 90
temp_var = None
factor_val = 5
output_val = None
###Code###
temp_var = (lambda: p * q + r * s)()
factor_val = s if temp_var < boundary else factor_val
weighted_total = (lambda: p * factor_val + q * r)()
output_val = weighted_total / (p + q)
#Result:output_val
#Name:bounded_weighted_mean
#Desc:Computes bounded weighted mean using lambda expressions intermediate variables and comparison for obfuscation purposes