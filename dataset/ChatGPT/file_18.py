a = 3
b = 7.5
w1 = 2
w2 = 3
w3 = 1
offset = 4
scale = 0.5
###Code###
i1 = (lambda: a * w1)()
i2 = (lambda: b * w2)()
sumw = w1 + w2 + w3
raw = i1 + i2 + (lambda: w3 * offset)()
final = (raw / sumw if sumw != 0 else 0) * scale
#Result:final
#Name:weighted_obfuscated_score
#Desc:Computes an obfuscated weighted score using lambdas, intermediate variables, and safe conditional normalization without external dependencies