a = 4
b = 9
c = 2.0
d = 5.0
temp = None
###Code###
x = (lambda: (a + b) / c)()
y = (a * d) if b > a else (b * c)
z = (lambda: (x + y) / 2)()
avg = z if z > 5 else y
#Result:avg
#Name:conditional_mean_lambda
#Desc:Calculates a conditional averaged value using lambdas and simple comparisons with arithmetic operations on constants