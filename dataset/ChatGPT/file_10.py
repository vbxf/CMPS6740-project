x = 4
y = 9
z = 2.5
scale = 1.2
bias = 3
###Code###
temp1 = x * scale
temp2 = y / z
adjusted = (lambda: temp1 + temp2)()
score = adjusted if adjusted > bias else bias
final_score = score / 2
#Result:final_score
#Name:scaled_comparison_score
#Desc:Computes scaled comparison average using lambda based conditional arithmetic operations with obfuscated numeric variable assignments
