a = 8
b = 3
c = 5.0
scale = 0.5
offset = 2
###Code###
diff = a - b
weighted = (lambda: diff * c * scale)()
adjusted = weighted / (b + offset)
final_score = adjusted if a > b else adjusted * scale
#Result:final_score
#Name:conditional_weight_score
#Desc:Calculates weighted conditional score using lambda expression and basic arithmetic operations on initialized numeric variables only