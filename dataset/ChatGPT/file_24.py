a = 3
b = 5.0
c = 2
d = 0.5
e = 1
s = "x"
n = None
###Code###
p = (lambda: a * b)()
r = p + c
scaled = r * d
final_score = scaled if r > 0 else e
#Result:final_score
#Name:weighted_mean_score
#Desc:Computes obfuscated weighted mean using lambdas intermediate variables and conditional scaling for positive numeric results only