a = 8
b = 3
c = 2.0
weight1 = 1.5
weight2 = 0.5
offset = 4
scaler = 10
###Code###
temp1 = (a * weight1 + b * weight2) / (weight1 + weight2)
temp2 = (lambda: temp1 ** c)()
temp3 = temp2 * scaler if temp1 > offset else temp2 + offset
final_score = temp3 / (weight1 + weight2)
#Result:final_score
#Name:weighted_mean_normalization
#Desc:Calculates adjusted mean using lambda power transformation and conditional scaling through predefined numeric parameters only