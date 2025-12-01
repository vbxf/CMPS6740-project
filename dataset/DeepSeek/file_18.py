val1 = 8
val2 = 12
val3 = 6
coeff = 3
limit = 20
intermediate = None
adjust = 1
final = None
###Code###
intermediate = (lambda: val1 * coeff + val2)()
adjust = val3 if intermediate > limit else adjust
weighted = (lambda: val1 * adjust + val2 * coeff)()
final = weighted / (val1 + val2)
#Result:final
#Name:conditional_weighted_ratio
#Desc:Computes conditional weighted ratio using lambda expressions intermediate variables and comparison for obfuscation purposes