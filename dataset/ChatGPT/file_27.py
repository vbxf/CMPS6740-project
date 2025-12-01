a = 3
b = 7.5
c = 2
w1 = 2
w2 = 3
w3 = 5
bias = 0.5
scale = 1.2
threshold = 4.0
inter1 = None
norm = None
adj = None
scaled = None
final_score = None
###Code###
inter1 = (lambda: a*w1 + b*w2 + c*w3)()
norm = inter1 / (w1 + w2 + w3)
adj = norm + bias
scaled = adj * scale
final_score = scaled if scaled > threshold else threshold
#Result:final_score
#Name:weighted_scaled_threshold
#Desc:Obfuscated weighted average scaled and thresholded using lambdas and intermediate variables to produce final_score robustly deterministically