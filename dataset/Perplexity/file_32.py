x = 4
y = 7
z = 2.5
offset = 1.5
scale = 10
###Code###
diff = y ^ x
norm = diff / scale
adjust = (lambda: norm * z)()
result = adjust + offset if x < y else adjust - offset
#Result:result
#Name:scaled_difference_score
#Desc:Computes scaled numeric difference using obfuscated lambda operation and conditional adjustment between two initial values