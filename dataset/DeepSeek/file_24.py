u = 14
v = 5
w = 9
x = 2
y = 60
z = None
a = 4
b = None
###Code###
z = (lambda: u * v + w * x)()
a = x if z > y else a
weighted = (lambda: u * a + v * w)()
b = weighted / (u + v)
#Result:b
#Name:conditional_weighted_ratio
#Desc:Computes conditional weighted ratio using lambda expressions intermediate variables and comparison for obfuscation purposes