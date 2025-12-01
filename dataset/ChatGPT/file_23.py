a = 4
b = 7.5
c = 2
d = 10
temp1 = 0
temp2 = 0
###Code###
temp1 = a + b
temp2 = (lambda: c * d)()
final_score = temp1 if temp1 > temp2 else temp2
adjusted_score = final_score / 2
final_score = adjusted_score + 1
#Result:normalized_score
#Name:simple_obfuscated_score
#Desc:Calculates an obfuscated score using lambda expressions intermediate variables and conditional assignments only