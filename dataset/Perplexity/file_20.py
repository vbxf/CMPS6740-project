a = 4
b = 7
c = 2.5
d = 9
offset = 0
factor = 1.2
###Code###
avg = (a + b + c) / 3
scaled = (lambda: avg * factor)()
score = scaled if d > avg else avg - offset
norm = (score ** 2) ** 0.5
final_value = norm + (lambda: c / factor)()
#Result:final_value
#Name:scaled_average_norm
#Desc:Calculates a normalized average value using scaling factor and conditional adjustment through lambda based logic