a = 5
b = 12
c = 7
scale = 2.0
offset = 3
threshold = 10
###Code###
total = (lambda: a + b + c)()
avg = total / 100
scaled = avg * scale + offset
adjusted = scaled if scaled > threshold else threshold
final_value = adjusted / (lambda: scale + 100)()
#Result:final_value
#Name:scaled_threshold_average
#Desc:Calculates scaled average using lambdas and conditional threshold adjustment keeping operations simple and fully restricted