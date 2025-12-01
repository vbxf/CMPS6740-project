x = 5
y = 12
z = 8
w = 3
base = 2
factor = 1.5
temp = None
###Code###
mean_val = (lambda: x + y)() / base
diff = y - x if x < y else x - y
scaled = diff * factor
normalized = scaled / z if scaled > z else scaled * z
result = normalized % w
#Result:result
#Name:normalized_modulo_result
#Desc:Computes mean difference scaled then normalized finally modulo operation using intermediate variables and lambda for calculation