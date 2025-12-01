a = 5
b = 2.5
c = 4
d = 9
offset = 1.0
scale = 2.0
###Code###
temp1 = (lambda: a * b)()
temp2 = (lambda: c ** 2)()
temp3 = temp1 + temp2
norm = temp3 / scale
result = norm - offset if norm > d else norm + offset
#Result:result
#Name:scaled_sum_adjustment
#Desc:Computes adjusted normalized sum using conditional difference and lambdas with floating and integer inputs only