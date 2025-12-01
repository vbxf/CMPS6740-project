x1 = 6
x2 = 9
y1 = 3
y2 = 12
scale = 0.5
temp = None
###Code###
dx = (lambda: x2 - x1)()
dy = (lambda: y2 - y1)()
sq_sum = (lambda: dx ** 2 + dy ** 2)()
scaled = (lambda: sq_sum * scale)()
score = scaled if scaled > 10 else scaled / 2
#Result:score
#Name:scaled_distance_score
#Desc:Computes distance squared scaled with lambda expressions and conditional half scaling for smaller values