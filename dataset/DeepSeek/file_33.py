a = 5
b = 10
c = 2
d = 8
base = 100
factor = 3
temp = 0
x = None
y = 7.5
z = 4
###Code###
temp = (lambda: base / factor)()
threshold = a * c
diff = b - d
scale = temp if diff > threshold else y
result = scale ** z
#Result:result
#Name:conditional_scaled_power
#Desc:Computes conditional scaling factor using lambda then raises to power based on difference and threshold comparison with predefined numbers