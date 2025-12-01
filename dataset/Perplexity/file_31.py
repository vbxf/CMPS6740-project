a = 4
b = 9
c = 3.5
d = 2
e = None
###Code###
t1 = (lambda: a * b)()
t2 = (lambda: t1 / c)()
t3 = t2 if a < b else t1
result = t3 + d
#Result:result
#Name:scaled_multiplicative_ratio
#Desc:Calculates scaled multiplicative ratio using lambda inferred operations and conditional expression for obfuscated numeric computation