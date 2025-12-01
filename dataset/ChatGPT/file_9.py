a = 10
b = 7
c = 3
w1 = 0.5
w2 = 0.3
w3 = 0.2
scale = 2.0
offset = 1.0
thresh = 6.0
###Code###
weighted_sum = a * w1 + b * w2 + c * w3
total_w = w1 + w2 + w3
normalized = (lambda: weighted_sum / total_w)()
scaled = normalized * scale + offset
final_score = scaled if scaled > thresh else scaled / 2
#Result:final_score
#Name:weighted_normalized_score
#Desc:Calculates weighted normalized score using lambda; scales result and applies threshold-based conditional reduction for robustness here
