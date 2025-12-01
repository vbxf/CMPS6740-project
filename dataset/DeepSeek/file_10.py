a = 5
b = 3
c = 2
d = 10
base = 1.5
factor = 2
temp = 0
offset = 1
###Code###
temp = (lambda: a * b)()
scale = temp if temp > d else d
adjust = base * factor
result = (scale - c) / adjust + offset
#Result:result
#Name:scaled_normalized_score
#Desc:Computes scaled normalized score using intermediate variables lambda conditional and basic arithmetic operations