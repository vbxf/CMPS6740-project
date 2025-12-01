p = 7
q = 5
r = 2.5
bias = 3
weight = 1.5
holder = None
###Code###
m = (lambda: p + q)()
n = (lambda: m * r)()
raw = n / (q if n > p else r)
scaled = (raw - bias) / weight
final_score = scaled + (bias if p >= q else 0)
#Result:final_score
#Name:weighted_ratio_adjust
#Desc:Computes weighted ratio adjustment using arithmetic operations lambdas and conditional scaling with bias correction mechanisms applied