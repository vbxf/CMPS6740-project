a = 3
b = 7
c = 4.0
d = 2
scale = 10.0
###Code###
sum_val = a + b
avg = (lambda: (sum_val + c) / 3)()
scaled = avg ** scale
adjusted = scaled if avg > d else scaled / 2
final_result = adjusted - c
#Result:final_result
#Name:scaled_average_computation
#Desc:Computes scaled average with lambda adjustment and conditional operation using predefined numeric constants for obfuscation purposes