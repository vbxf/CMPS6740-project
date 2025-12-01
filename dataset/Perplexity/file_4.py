x = 8
y = 3
z = 4.5
shift = 2
scale = 1.5
aux = None
###Code###
p = (lambda: x - y)()
q = (lambda: z * scale)()
mid = (p + q) / (x if p > q else y)
norm = (mid - shift) / scale
adjusted = norm + (shift if z < x else 0)
#Result:adjusted
#Name:scaled_difference_ratio
#Desc:Calculates scaled difference ratio with lambda operations and conditional normalization based on predefined numerical variable comparisons