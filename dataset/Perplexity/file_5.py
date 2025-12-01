x = 4
y = 7
z = 3
scale = 2.0
offset = 1.5
threshold = 10
temp = None
###Code###
sum_val = x + y + z
weighted = sum_val * scale
adjusted = weighted / (lambda: scale + offset)()
final_score = adjusted if weighted < threshold else weighted - offset
#Result:final_score
#Name:scaled_threshold_score
#Desc:Calculates adjusted scaled total and conditional threshold reduction using lambda based computation with numeric variables only