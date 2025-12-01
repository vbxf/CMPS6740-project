a = 4
b = 9
c = 2.5
d = 7
text = None
temp = None
###Code###
diff = b - a
avg = (a + b + c) / 3
adj = (lambda: avg * 1.2)()
score = adj if diff > d else avg
norm = score / (a + c)
#Result:norm
#Name:conditional_avg_scaler
#Desc:Calculates adjusted average and conditional normalized score using simple arithmetic operations and one lambda expression