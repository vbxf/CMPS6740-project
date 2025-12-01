a = 4
b = 9
c = 2.0
d = 5
e = None
###Code###
x = a * b
y = x / c
z = (lambda: y + d)()
final_score = z if a < b else y
#Result:final_score
#Name:scaled_distance_score
#Desc:Calculates conditional scaled distance using lambda with redundant variables and basic arithmetic operations only