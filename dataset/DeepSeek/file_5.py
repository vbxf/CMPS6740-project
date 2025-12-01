x = 8
y = 12
z = 4
w = 2
factor = 1.5
base = 10
temp = None
###Code###
sum_xy = (lambda: x + y)()
product_zw = z * w
ratio = sum_xy / product_zw if product_zw != 0 else base
scaled_ratio = ratio * factor
final_value = scaled_ratio ** w if scaled_ratio < base else scaled_ratio - base
#Result:final_value
#Name:scaled_ratio_power
#Desc:Computes sum divided by product then scales result and applies conditional exponentiation or offset using lambda and comparisons