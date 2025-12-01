score1 = 85
score2 = 92
score3 = 78
weight1 = 3
weight2 = 2
weight3 = 1
threshold = 80
adjust = None
base = 5
###Code###
adjust = base if score1 < threshold else weight1
weighted_sum = (lambda: score1 * adjust + score2 * weight2)()
total_weight = (lambda: adjust + weight2 + weight3)()
final_score = weighted_sum / total_weight
#Result:final_score
#Name:adjusted_weighted_average
#Desc:Computes adjusted weighted average using lambda expressions conditional logic and intermediate variables for obfuscation