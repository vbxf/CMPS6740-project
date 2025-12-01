c1 = 8
c2 = 12
c3 = 6
c4 = 3
threshold = 80
temp_val = None
multiplier = 4
final_result = None
###Code###
temp_val = (lambda: c1 * c2 + c3 * c4)()
multiplier = c4 if temp_val < threshold else multiplier
weighted_sum = (lambda: c1 * multiplier + c2 * c3)()
final_result = weighted_sum / (c1 + c2)
#Result:final_result
#Name:conditional_weighted_mean
#Desc:Computes conditional weighted mean using lambda expressions intermediate variables and comparison for obfuscation purposes