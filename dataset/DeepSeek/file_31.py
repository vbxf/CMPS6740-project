a = 5
b = 3
c = 2
d = 10
base = 1.5
factor = 2
temp = 0
###Code###
temp = (lambda: a * b)()
scale = temp if temp > d else d
offset = base * factor
result = (scale - offset) / c
#Result:result
#Name:scaled_offset_normalization
#Desc:Computes normalized value after scaling comparison with threshold using intermediate variables and lambda for obfuscation purposes