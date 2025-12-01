a = 4
b = 7.5
c = 2
d = 0
e = 1
f = 3.5
g = 10
###Code###
temp1 = (lambda: a * b)()
temp2 = temp1 / c
temp3 = temp2 if d < e else temp2 + f
final_score = temp3 % g
#Result:final_score
#Name:obfuscated_weighted_score
#Desc:Calculates obfuscated weighted score using lambdas and conditional assignments over predefined variables only