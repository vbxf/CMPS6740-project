a = 3
b = 5
w1 = 0.6
w2 = 0.4
offset = 1.0
scale = 2.0
unused = None
s = None
###Code###
m = (lambda: a * w1 + b * w2)()
adj = m + offset
clamped = adj if adj < 10 else 10
final_score = (lambda: (clamped - a) / scale)()
#Result:final_score
#Name:weighted_score_obf
#Desc:Computes an obfuscated weighted score with lambda and clamp, using intermediate variables and simple arithmetic operations