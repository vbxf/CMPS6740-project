x = 6
y = 8
z = 10
w = 2
cutoff = 50
inter = None
factor = 4
output = None
###Code###
inter = (lambda: x * y + z * w)()
factor = w if inter < cutoff else factor
weighted = (lambda: x * factor + y * w)()
result = weighted / (x + y)
#Result:result
#Name:conditional_weighted_mean
#Desc:Computes conditional weighted mean using lambda expressions intermediate variables and comparison for obfuscation purposes