x = 55
y = 30
z = 20
w = 3
factor = 2
base = 10
temp = None
###Code###
sum_xy = (lambda: x + y)()
diff_yz = y - z
ratio = sum_xy / diff_yz if diff_yz != 0 else base
scaled = ratio * factor
final_value = scaled ** w if scaled > base else scaled + w
#Result:final_value
#Name:scaled_power_adjustment
#Desc:Computes sum difference ratio then scales and applies conditional power operation using lambda and intermediate variables for obfuscation