first = 10
second = 8
third = 6
fourth = 2
max_val = 50
inter_med = None
scale_fact = 4
end_result = None
###Code###
inter_med = (lambda: first * second + third * fourth)()
scale_fact = fourth if inter_med < max_val else scale_fact
weighted_sum = (lambda: first * scale_fact + second * third)()
end_result = weighted_sum / (first + second)
#Result:end_result
#Name:max_bounded_weighted_mean
#Desc:Computes max bounded weighted mean using lambda expressions intermediate variables and comparison for obfuscation purposes