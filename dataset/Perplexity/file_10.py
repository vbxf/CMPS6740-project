a = 7
b = 3
c = 2.0
d = 10
e = None
f = "ignore"
###Code###
temp1 = a * b
temp2 = (lambda: temp1 / c)()
temp3 = temp2 + d
final_value = temp3 if a > b else temp1 - d
#Result:final_value
#Name:scaled_ratio_selector
#Desc:Calculates scaled ratio then conditionally selects adjusted result using simple comparison and lambda based evaluation