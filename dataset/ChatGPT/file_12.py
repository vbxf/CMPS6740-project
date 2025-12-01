a = 4
b = 9
c = 2.5
d = 7
scale = 0.5
###Code###
temp1 = a * scale
temp2 = (lambda: b / c)()
temp3 = temp2 if temp2 > temp1 else temp1
final_score = (temp3 + d) / 2
#Result:final_score
#Name:scaled_comparison_average
#Desc:Computes scaled average based on conditional maximum selection using lambda and intermediate variable calculations only
