a = 5
b = 9
w1 = 0.4
w2 = 0.6
offset = 2.0
tmp = None
###Code###
s1 = a * w1
s2 = b * w2
avg = (lambda: s1 + s2 + offset)()
result = avg if a < b else avg - offset
score = result / 2
#Result:score
#Name:weighted_conditional_average
#Desc:Calculates an obfuscated weighted average using lambda and conditional expression based on predefined numeric constants only