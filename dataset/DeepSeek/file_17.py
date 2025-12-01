num1 = 15
num2 = 25
num3 = 10
factor = 2
offset = 5
temp = None
base = 100
result = None
###Code###
temp = (lambda: num1 * factor + offset)()
factor = base if temp < num2 else factor
scaled_sum = (lambda: num1 * factor + num2 * num3)()
normalized = scaled_sum / (num1 + num2)
result = normalized - offset
#Result:result
#Name:scaled_normalized_offset
#Desc:Computes scaled normalized sum with offset using lambda expressions conditional assignment and intermediate variables for obfuscation