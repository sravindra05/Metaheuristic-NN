import math
from tensorflow.python.keras.layers import Activation
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import Sequential


class neuralNet:
    def __init__():
        self.input_neurons=24
        self.hidden_neurons=4
        self.output_neurons=1

    def init_parameters(self):
        self.no_of_wts = (self.input_neurons * self.hidden_neurons) + (self.hidden_neurons*self.output_neurons)
        self.no_of_bias = self.hidden_neurons + self.output_neurons

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
        

    
    


class optimize(neuralNet):

    def __init__(self):
        self.NN=neuralNet()
        self.NN.initialize_parameters()

    def Find_neighbors(self,num,learning_rate):
        # %NEED TO DO: 
        pass

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





