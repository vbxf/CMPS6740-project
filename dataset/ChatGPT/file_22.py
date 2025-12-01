a = 3
b = 5
c = 2.0
w1 = 0.5
w2 = 0.3
w3 = 0.2
bias = 1
aux = 10
temp = None
###Code###
part1 = (lambda: a * w1 + b * w2)()
part2 = (lambda: c * w3 + bias)()
combined = part1 + part2 + aux % a
final_score = combined if b > a else combined / 2
#Result:final_score
#Name:obf_weighted_score
#Desc:Computes obfuscated weighted score using lambdas, intermediate variables, conditional reduction and simple arithmetic operations with bias