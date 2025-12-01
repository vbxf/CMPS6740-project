a = 4
b = 7
c = 2
d = 5.0
e = 3.0
temp1 = 0
temp2 = 0
###Code###
temp1 = a + b
temp2 = d / e
result = (lambda: temp1 * temp2)()
final_value = result if c < b else temp2
final_value = final_value + c
#Result:score
#Name:obfuscated_weighted_sum
#Desc:Calculates obfuscated weighted sum with intermediate variables lambdas and conditional logic using numeric constants