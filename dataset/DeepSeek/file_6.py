x = 10
y = 5
z = 2
factor = 3
base = 1
temp = None
offset = 7
###Code###
threshold = (lambda: x * factor)()
scaled_y = y * z
adjustment = base if threshold > scaled_y else offset
weighted_sum = (x * factor) + (scaled_y * z)
final = (weighted_sum - adjustment) / z
#Result:final
#Name:weighted_scaled_adjustment
#Desc:Computes a weighted sum with scaling and conditional adjustment using intermediate variables and a lambda for threshold calculation