import math

class NN_helpers:
    def weighted_average(inputs,weights,bias=0):
        if(len(inputs)!=len(weights)):
            raise Exception("Number of weights and inputs must be the same")
        else:
            sum=0
            for i in range(len(inputs)):
                sum+=weights[i]*inputs[i]
            sum=sum - bias
            return sum

    def Relu(inputs,weights,bias):
        sum = weighted_average(inputs,weights,bias)
        if(sum<0):
            return 0
        else:
            return sum

    def Sigmoid(inputs,weights,bias):
        sum = weighted_average(inputs,weights,bias)
        sum = math.exp(-1*sum)
        sum = 1 + sum
        sum = 1/sum
        return(sum)

    # Heuristic
    # %WRONG: Okay I think the function part is completely wrong - we need to go through the layers
    def Loss(inputs,weights,bias,function,true_class):
        pred_class = function(inputs, weights,bias)
        loss = true_class - pred_class
        return loss

    def Total_loss(inputs,weights,bias,function,true_class):
        loss=0
        for i in range(len(inputs)):
            loss += Loss(inputs[i],weights,bias,function,true_class)
        loss = some_aggregate(loss)  # %WRONG: Dont know loss function!!!!!!!!!!!!
        return(loss)


class optimize(NN_helpers):

    def __init__(self):
        # NN specification 
        print("How many neurons in input layer: ")
        self.input_neurons= int(input())
        print("Activation function: ")
        self.input_activation_fn=input().toLower()

        print("How many hidden layers:")
        self.hidden_layers=int(input())
        self.HL_neuron_count=[]
        self.HL_activation_fn=[]
        for i in range(self.hidden_layers):
            print("How many layers in hidden layer ",self.hidden_layer+1,":",sep="")
            self.HL_neuron_count.append(int(input()))
            print("Activation function for hidden layer ",self.hidden_layer+1,":",sep="")
            self.HL_activation_fn.append(input()).toLower()

        print("How many neurons in output layer: ")
        self.output_neurons= int(input())
        print("Activation function: ")
        self.output_activation_fn=input()

    def initialize_parameters(self):
        # %NEED TO DO: initialize weights and bias
        pass

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
        initialize_parameters()
        inputs = csv [:][0:-1]
        true_class = csv[:][-1]

        # Find loss for initialized weights
        loss = Total_loss(inputs,self.weights,self.bias,function*,true_class) # %WRONG: function need to see what to do

        iter_counter=0
        while(iter_counter < max_iter):
            neighbors = Find_neighbors(num,learning_rate) #should return new weights and bias
            min_loss = loss

            for neighbor in neighbours:
                l = Total_loss(inputs,neighbors[0],neighbors[1],function*,true_class)
                if(l>=loss): 
                    # basically pop that neighbor out
                    neighbors.remove(neighbor) 
                else:
                    # finding the least loss/error
                    if(l < min_loss[1]):
                        min_loss = (neighbor,l)

            if(len(neighbors))==0:
                Levi_flight()

            else:
                neighbor = min_loss[0]
                if(Converged(neighbor[0],self.weights,0.0001) and Converged(neighbor[1],self.bias,0.0001):
                    return(self.weights,self,bias)
                self.weights = neighbor[0]
                self.bias = neighbor[1]





