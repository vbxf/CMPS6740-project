a = 3
b = 5
c = 2
w1 = 0.5
w2 = 1.5
w3 = 1
offset = 1
scale = 2
###Code###
tmp1 = (lambda: a * w1 + b * w2)()
tmp2 = (lambda: tmp1 + c * w3)()
avg = tmp2 / (w1 + w2 + w3)
final = avg * scale if offset < a else avg / scale
#Result:final
#Name:weighted_mean_score
#Desc:Obfuscated weighted average computed with lambdas and conditional scaling using predefined numeric variables and intermediate temporaries