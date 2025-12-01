x = 10
y = 4
z = 2
base = 3.0
offset = 1
temp = None
scale = 0.5
factor = 2
###Code###
power_check = (lambda: base ** z)()
threshold = x if power_check > y else y
weighted_avg = (x * scale) + (y * scale)
adjusted = weighted_avg / threshold
result = adjusted * factor
#Result:result
#Name:scaled_weighted_average
#Desc:Computes scaled weighted average using power comparison lambda and intermediate variables for algorithmic obfuscation with numeric operations