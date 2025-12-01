a = 10
b = 20
c = 5
d = 15
e = 25
f = None
g = 2
h = 3
###Code###
f = (lambda: a * b - c)()
g = d if f > e else h
weighted = (lambda: a * g + b * h)()
average = weighted / (a + b)
result = average * c
#Result:result
#Name:weighted_average_scaled
#Desc:Computes scaled weighted average using lambda expressions conditional assignment and intermediate variables for obfuscation purposes