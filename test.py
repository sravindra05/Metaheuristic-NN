
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

# NN specification 
        # print("How many neurons in input layer: ")
        # self.input_neurons= int(input())
        # print("Input layer Activation function: ")
        # self.input_activation_fn=input().toLower()

        '''
        print("How many hidden layers:")
        self.hidden_layers=int(input())
        self.HL_neuron_count=[]
        self.HL_activation_fn=[]
        for i in range self.hidden_layers():
            print("How many layers in hidden layer ",self.hidden_layer+1,":",sep="")
            self.HL_neuron_count.append(int(input()))
            print("Activation function for hidden layer ",self.hidden_layer+1,":",sep="")
            self.HL_activation_fn.append(input()).toLower()
        '''
        # print("How many neurons in hidden layer: ")
        # self.hidden_neurons= int(input())
        # print("Hidden Layer Activation function: ")
        # self.hidden_activation_fn=input().toLower()

        # print("How many neurons in output layer: ")
        # self.output_neurons= int(input())
        # print("Output layer Activation function: ")
        # self.output_activation_fn=input().toLower()

def Relu(self,inputs,wt,b):
        Sum = weighted_average(inputs,wt,b)
        if(Sum<0):
            return 0
        else:
            return Sum

    def Sigmoid(self,inputs,wt,b):
        Sum = weighted_average(inputs,wt,b)
        Sum = math.exp(-1*Sum)
        Sum = 1 + Sum
        Sum = 1/Sum
        return(Sum)


def Loss(self,input,wt,b,true_class):
        # hidden layer forward feed
        hidden = []
        for i in range(self.hidden_neurons):
            WT = wt[0][i]
            B = b[0][i]
            if self.hidden_activation_fn == 'relu':
                Sum = self.Relu(input,wt,b)
            elif self.output_activation_fn == 'sigmoid':
                Sum = self.Sigmoid(input,wt,b)
            else:
                raise Exception("Activation function not supported")
            hidden.append(Sum)
            
        output = []
        # for i in range(self.output_neurons):
        WT = wt[1]
        B = b[1]
        if self.output_activation_fn == 'relu':
            Sum = self.Relu(hidden,wt,b)
        elif self.output_activation_fn == 'sigmoid':
            Sum = self.Sigmoid(hidden,wt,b)
        else:
            raise Exception("Activation function not supported")
            # output.append((i,Sum))

        error = true_class - Sum
        error = -1 * (true_class * math.log(Sum)+((1-true_class)*math.log(1-Sum)))
        return error

    def Total_loss(self,inputs,wt,b,true_class):
        error = 0
        for i in range(len(inputs)):
            error+ = Loss(inputs[i],wt,b,true_class[i])
        return(error)

def weighted_average(self,data,wt,b):
        if(len(input)!=len(wt)):
            raise Exception("Number of weights and inputs must be the same")
        else:
            Sum=0
            for i in range(len(data)):
                Sum+=wt[i]*data[i]
            Sum=Sum - b
            return Sum

    # Heuristic

def Find_neighbor():
    rand = random.randrange(0,self.no_of_wts)
    w = flatten(self.weights)
    for i in range(rand):
        r=random.randrange(0,self.no_of_wts)
        w[r]+= self.learning_rate#increment here

    rand = random.randrange(0,self.no_of_bias)
    b = flatten(self.bias)
    for i in range(rand):
        r=random.randrange(0,self.no_of_bias)
        b[r]+= self.learning_rate#increment here
    return(w,b)
    
