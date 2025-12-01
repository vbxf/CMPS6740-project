a = 3
b = 4.5
c = 2
w1 = 0.5
w2 = 1.5
w3 = 1.0
scale = 2.0
bias = 0.1
thr = 3.0
s = "unused"
z = None
###Code###
score1 = a * w1 + b * w2
score2 = (lambda: score1 + c * w3)()
norm = score2 / (w1 + w2 + w3)
adjusted = norm * scale if norm > thr else norm / scale
final = (lambda: adjusted + bias)()
#Result:final
#Name:weighted_mean_score
#Desc:Obfuscated weighted mean calculation using lambdas, intermediate variables, and conditional scaling to produce final adjusted score.