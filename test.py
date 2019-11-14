
file = open('/Users/pragnya/Documents/GitHub/Metaheuristic-NN/result1.txt','r')
lines = file.readlines()
metrics = lines[-11]
print(metrics)
metrics = metrics.split(" - ")
accuracy = metrics[3]
loss = metrics[2]
time = lines[-1]
print(accuracy)