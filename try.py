import math

class neuralNet:
    def __init__():
        self.input_neurons=24
        self.hidden_neurons=4
        self.output_neurons=1

    def init_parameters(self):
        no_of_wts = (self.input_neurons * self.hidden_neurons) + (self.hidden_neurons*self.output_neurons)
        no_of_bias = self.hidden_neurons + self.output_neurons

        w=[]
        b=[]
        
        for i in range(no_of_wts):
            w.append(random.uniform(-2,2))

        for i in range(no_of_bias):
            b.append(random.uniform(-2,2))

        self.weights = unflatten(w)
        self.bias = unflatten(b)


    def unflatten(self,array):
        i=0
        w=[[],[]]
        while(i<(self.input_neurons*self.hidden_neurons)):
            w[0].append(list(array[i:i+self.input_neurons]))
            i+=self.input_neurons
        while(i<(self.hidden_neurons*self.output_neurons)):
            w[1].append(list(array[i:i+self.hidden_neurons]))
            i+=self.hidden_neurons
        return(w)

    def flatten(self,array):
        pass
        

    def weighted_average(self,data,wt,b):
        if(len(input)!=len(wt)):
            raise Exception("Number of weights and inputs must be the same")
        else:
            Sum=0
            for i in range(len(data)):
                Sum+=wt[i]*data[i]
            Sum=Sum - b
            return Sum

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

    def Softmax(self,inputs,wt,b):

    # Heuristic
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


class optimize(neuralNet):

    def __init__(self):
        self.NN=neuralNet()
        self.NN.initialize_parameters()

    def Find_neighbors(self,num,learning_rate):
        # %NEED TO DO: 

    def Converged(self,a,b,lim):
        if(len(a)!=len(b)):
            raise Exception("Unequal length arrays compared")
        else:
            for i in range(len(a)):
                if(a[i]-b[i]>lim):
                    return False
            return True

    def Levi_flight():
        # %NEED TO DO
        pass()

    def eagle_strategy(self,csv,max_iter=math.inf):
        inputs = csv [:][0:-1]
        true_class = csv[:][-1]

        # Find loss for initialized weights
        loss = Total_loss(inputs,self.weights,self.bias,true_class)

        iter_counter=0
        while(iter_counter < max_iter):
            neighbors = Find_neighbors(num,learning_rate) #should return new weights and bias
            min_loss = [[self.weights,self.bias],loss)

            for neighbor in neighbours:
                l = Total_loss(inputs,neighbors[0],neighbors[1],true_class)
                if(l>=loss): 
                    # basically pop that neighbor out
                    neighbors.remove(neighbor) 
                else:
                    # finding the least loss/error
                    if(l < min_loss[1]):
                        min_loss = ([neighbor[0],neighbor[1]],l)

            if(len(neighbors))==0:
                Levi_flight()

            else:
                neighbor = min_loss[0]
                if(Converged(neighbor[0],self.weights,0.0001) and Converged(neighbor[1],self.bias,0.0001):
                    return(self.weights,self,bias)
                self.weights = neighbor[0]
                self.bias = neighbor[1]





