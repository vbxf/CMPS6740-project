a = 3
b = 7
c = 2.0
offset = 1
scale = 0.5
###Code###
temp1 = (a + b) / 2
temp2 = (lambda: (temp1 * scale) + offset)()
adjusted = temp2 if temp2 > c else c
final_score = (adjusted + c) / 2
#Result:final_score
#Name:normalized_average_score
#Desc:Calculates normalized average using lambda adjustment and conditional rule to ensure minimum scaling threshold value