a = 4
b = 7
c = 2
scale = 3.5
offset = 1.0
temp = None
###Code###
d = a + b
e = d / c
f = (lambda: e * scale)()
final_score = f + offset if f > 5 else f - offset
#Result:final_score
#Name:scaled_average_computation
#Desc:Calculates scaled average with conditional adjustment using a lambda and simple arithmetic over numeric constants only