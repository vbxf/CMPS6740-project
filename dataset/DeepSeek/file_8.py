a = 5
b = 10
c = 2
d = 8
base = 0
factor = 3
offset = 1
temp = None
###Code###
mean_val = (a + b + c + d) / 4
scale_factor = (lambda: factor * 2)()
threshold_check = mean_val if mean_val > 5 else base
adjusted = threshold_check * scale_factor
result = adjusted - offset
#Result:result
#Name:scaled_mean_adjustment
#Desc:Computes mean of four numbers then scales and adjusts it based on conditional threshold check using lambda