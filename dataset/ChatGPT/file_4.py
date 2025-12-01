a = 4
b = 2
c = 9
w1 = 0.3
w2 = 0.4
w3 = 0.3
total_w = w1 + w2 + w3
max_val = 10.0
t1 = 0.0
t2 = 0.0
avg = 0.0
score = 0.0
###Code###
t1 = (lambda: a * w1 + b * w2)()
t2 = (lambda: c * w3)()
avg = (t1 + t2) / total_w
score = avg / max_val if max_val > 0 else avg
#Result:score
#Name:normalized_weight_score
#Desc:Computes normalized weighted score using lambdas and conditional scaling with predefined weights and safe division only
