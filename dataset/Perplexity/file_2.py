a = 5
b = 2
c = 3.0
offset = 1
factor = 4.0
temp = None
###Code###
u = (lambda: a ** b)()
v = (lambda: c * factor)()
mix = (u + v) / (b if u > v else a)
norm = (mix - offset) / factor
final_value = norm + (offset if b < a else 0)
#Result:final_value
#Name:quadratic_scale_balance
#Desc:Performs quadratic scaling blend using exponentiation normalization and conditional adjustment based on variable magnitude comparison