x = 4
y = 9
z = 2.0
offset = 1
temp = None
###Code###
diff = y - x
ratio = diff / z
scaled = (lambda: ratio * 3)()
final = scaled + offset if y > x else offset - scaled
#Result:final
#Name:scaled_difference_score
#Desc:Computes scaled difference using conditional logic and zero parameter lambda for basic numeric manipulation