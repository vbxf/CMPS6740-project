a = 4
b = 9
c = 2.5
d = 7
scale = 1.2
temp = None
###Code###
diff = b - a
base = (lambda: diff * c)()
adjusted = base / scale
final = adjusted if d > base else base / d
result = (lambda: final + c)()
#Result:result
#Name:scaled_difference_rule
#Desc:Calculates modified scaled difference using lambdas and conditional logic with predefined numeric assignments and arithmetic operations