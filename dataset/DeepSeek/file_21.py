m = 5
n = 12
p = 8
q = 3
bound = 40
tmp = None
mult = 2
res = None
###Code###
tmp = (lambda: m * n + p * q)()
mult = q if tmp < bound else mult
scaled = (lambda: m * mult + n * q)()
res = scaled / (m + n)
#Result:res
#Name:bounded_scaled_ratio
#Desc:Computes bounded scaled ratio using lambda expressions conditional logic and intermediate variables for obfuscation purposes