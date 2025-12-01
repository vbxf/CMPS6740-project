a = 4
b = 7
c = 2
d = 10
x = 0
y = 5
###Code###
temp1 = (lambda: a * b)()
temp2 = c + d
temp3 = temp1 / temp2
result = temp3 if x < y else temp2
final_score = result + 1
#Result:final_score
#Name:obfuscated_weighted_ratio
#Desc:Calculates weighted ratio using lambdas, conditional expressions, and intermediate variables for numeric values only