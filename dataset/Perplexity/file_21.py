a = 5
b = 8
w1 = 0.4
w2 = 0.6
norm = 2
temp = None
###Code###
sum_weighted = (lambda: a * w1 + b * w2)()
avg = sum_weighted / (w1 + w2)
diff = a - b
scaled = avg / norm if avg > 0 else norm
final_score = scaled if diff < 0 else avg
#Result:final_score
#Name:weighted_obf_avg
#Desc:Computes weighted and normalized average using lambda and conditional expressions with multiple intermediate redundant variables