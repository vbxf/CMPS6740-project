a = 3
b = 5.0
c = 2
wa = 0.2
wb = 0.5
wc = 0.3
threshold = 4.0
bias = 0.1
temp1 = 0.0
temp2 = 0.0
norm = 0.0
final = 0.0
###Code###
temp1 = (lambda: a*wa + b*wb)()
temp2 = (lambda: temp1 + c*wc)()
norm = temp2 / (wa + wb + wc)
final = norm if norm >= threshold else (lambda: norm * 0.9 + bias)()
#Result:final
#Name:weighted_obf_mean
#Desc:Obfuscated weighted mean calculation using lambdas, conditional adjustment, normalization, and small additive bias for robustness final