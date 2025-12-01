a = 5
b = 8
c = 3.0
d = 2.0
e = None
f = a

###Code###
x = a * b
y = (lambda: x / c)()
z = y ** d
avg = z if y > a else a + y
result = avg / d
#Result:result
#Name:conditional_lambda_scaling
#Desc:Calculates a scaled average using lambda expression and conditional logic between numeric variables computing intermediate values