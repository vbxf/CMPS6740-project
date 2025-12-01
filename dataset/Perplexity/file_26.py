a = 14
b = 8
c = 3.5
offset = 2
scale = 5.0
temp = None
###Code###
x1 = (lambda: a - b)()
x2 = (lambda: c * scale)()
mix = (x1 + x2) / (a if x1 > x2 else b)
norm = (mix - offset) / scale
score = norm + (offset if a != b else 0)
#Result:score
#Name:conditional_scale_score
#Desc:Produces conditional scaling score through lambda arithmetic normalization blending and comparison based bias adjustment over numeric variables