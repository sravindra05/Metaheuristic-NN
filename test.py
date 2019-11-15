
file = open('/Users/pragnya/Documents/GitHub/Metaheuristic-NN/result1.txt','r')
lines = file.readlines()
metrics = lines[-11]
print(metrics)
metrics = metrics.split(" - ")
accuracy = metrics[3]
loss = metrics[2]
time = lines[-1]
print(accuracy)

wts=[[]]
        b=[[]]
        for j in range(self.hidden_neurons):
            neuron_wt=[]
            b[0].append(random)
            for k in range(self.input neurons):
                neuron_wt.append(random.uniform(-2,2))
            wts[0].append(neuron_wt)

        for j in range(self.hidden_neurons)
