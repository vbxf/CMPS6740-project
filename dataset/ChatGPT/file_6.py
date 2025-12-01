p = 6
q = 4
r = 10
alpha = 0.25
beta = 0.75
limit = 5.0
mix = 0.0
adjusted = 0.0
result = 0.0
###Code###
mix = (lambda: p * alpha + q * beta)()
adjusted = (lambda: mix + r / 2)()
result = adjusted if adjusted < limit else adjusted / limit
#Result:result
#Name:bounded_weight_mix
#Desc:Computes bounded weighted mixture using lambdas and conditional division ensuring upper limit normalization of values
