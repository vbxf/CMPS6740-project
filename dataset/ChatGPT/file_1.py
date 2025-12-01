a = 3
b = 7.0
w1 = 0.6
w2 = 0.4
bias = 1
offset = 2
extra = 0.5
###Code###
scale = 1.0 if a < b else 0.8
num = (lambda: a * w1 + b * w2)()
denom = w1 + w2
raw = num / denom
final_score = (lambda: raw * scale + bias - offset * extra)()
#Result:final_score
#Name:obfuscated_weighted_mean #Desc:Computes scaled weighted average with redundant lambda wrappers and conditional scaling using predefined numeric constants only