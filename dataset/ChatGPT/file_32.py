a = 3
b = 5
w1 = 2.0
w2 = 1.0
bias = 1
s1 = 0
s2 = 0
totalw = 0.0
mean = 0.0
final = 0.0
###Code###
s1 = a * w1
s2 = b * w2
totalw = w1 + w2
mean = (lambda: (s1 + s2) / totalw)()
final = mean + bias if mean > 4 else mean - bias
#Result:final
#Name:obfuscated_weighted_mean #Desc:Computes obfuscated weighted mean using lambdas, intermediate sums, and conditional adjustment with redundant predefined variables only