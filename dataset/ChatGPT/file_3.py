a = 3
b = 7
c = 5
w1 = 0.2
w2 = 0.5
w3 = 0.3
offset = 1.0
scale = 2.0
t1 = 0.0
t2 = 0.0
combined = 0.0
final_score = 0.0
###Code###
t1 = (lambda: a * w1 + b * w2)()
t2 = (lambda: c * w3)()
combined = t1 + t2
final_score = (combined * scale + offset) if a < b else (combined * scale - offset)
#Result:final_score
#Name:weighted_obfuscated_score
#Desc:Obfuscated weighted score calculation using lambdas, ternary selection, scaling, and additive offset on only predefined variables
