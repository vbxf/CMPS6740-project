p = 12
q = 3
r = 7
s = 2
t = 5
u = None
v = 4
w = 1
###Code###
u = (lambda: p % q + r)()
v = s if u > t else w
discriminant = (lambda: v * v - 4 * s * t)()
root_part = discriminant / (2 * s)
final = root_part + v
#Result:final
#Name:quadratic_discriminant_calc
#Desc:Computes quadratic discriminant component using lambda expressions conditional logic and intermediate variables for obfuscation purposes