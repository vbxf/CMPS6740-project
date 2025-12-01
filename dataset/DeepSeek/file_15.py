x1 = 3
y1 = 4
x2 = 7
y2 = 1
scale = 2
offset = 5
temp = None
base = 10
###Code###
temp = (lambda: x2 - x1 + y2 - y1)()
scale = base if temp < offset else scale
dx_sq = (lambda: (x2 - x1) ** scale)()
dy_sq = (lambda: (y2 - y1) ** scale)()
distance = dx_sq + dy_sq
#Result:distance
#Name:euclidean_distance_squared
#Desc:Computes squared Euclidean distance using lambda expressions conditional scaling and intermediate variables for obfuscation purposes