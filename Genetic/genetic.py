from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler as SC
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import log_loss
from scipy.stats import uniform
from scipy.stats import levy
import mlrose
from opt_probs import ContinuousOpt
from neural import NeuralNetwork
from datetime import datetime
import random
import copy
from sklearn import preprocessing
import matplotlib.pyplot as plt


l = []


def generateColumns(start, end):
    for i in range(start, end+1):
        l.extend([str(i)+'X', str(i)+'Y'])
    return l


eyes = generateColumns(1, 12)

# reading in the csv as a dataframe
df = pd.read_csv(
    "Eyes.csv")

# selecting the features and target
X = df[eyes]
y = df['truth_value']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.10, random_state=42)

# Data Normalization
sc = SC()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

X_train, y_train, X_test, y_test = np.array(X_train), np.array(
    y_train), np.array(X_test), np.array(y_test)

# print(df_results)

nn = NeuralNetwork(hidden_nodes=[4], activation='relu',
                   algorithm='hi', max_iters=500,
                   bias=True, is_classifier=True, learning_rate=0.1,
                   early_stopping=False, clip_max=2, max_attempts=10,
                   random_state=3)

def Find_neighbors(wts,lr):
    r = random.randrange(0,len(wts))
    w=copy.deepcopy(wts)
    for i in range(r):
        ind = random.randrange(0,len(wts))
        w[ind]+= lr * random.choice([-1,1])
    # print(w)
    return w


def normalize(array):
    sm = sum(array)

    ret = []
    for e in array:
        ret.append(e/sm)
    return ret


def genetic_algorithm(wts,pop_size=200, mutation_prob=0.1, max_attempts=10,max_iters=np.inf,lr = 0.3):
    def reproduce(parent1,parent2,mutation_prob):
        n = np.random.randint(len(parent1))
        child = np.array([0]*len(parent1))
        # print(parent1)
        child[0:n+1] = parent1[0:n+1]
        child[n+1:] = parent2[n+1:]
        # print(child)
        rand = np.random.uniform(size=len(parent1))
        mutate = np.where(rand < mutation_prob)[0]
        
        for i in mutate:
            child[i] = np.random.uniform(-3,3)
        # print(child)
        return child
    
    # if curve:
    #     fitness_curve = []
    
    population=[]
    for i in range(pop_size):
        w = Find_neighbors(wts,lr)
        population.append(w)

    attempts = 0
    iters = 0

    # Calculate breeding probabilities
    breeding_prob=[]
    for i in range(pop_size):
        nn.fit(X_train, y_train, population[i])
        y_train_pred = nn.predict(X_train)
        acc1 = accuracy_score(y_train, y_train_pred)
        breeding_prob.append(acc1)

    # Loss = []

    while (attempts < max_attempts) and (iters < max_iters):
        iters += 1

        bp = normalize(breeding_prob)
        
        # Create next generation of population
        next_gen = []
        child_fit=[]
        child_loss=[]

        for _ in range(pop_size):
            # Select parents
            selected = np.random.choice(pop_size, size=2,
                                        p=bp)
            parent_1 = population[selected[0]]
            parent_2 = population[selected[1]]

            # Create offspring
            child = reproduce(parent_1, parent_2, mutation_prob)
            next_gen.append(child)
            nn.fit(X_train, y_train, child)
            y_train_pred = nn.predict(X_train)
            acc1 = accuracy_score(y_train, y_train_pred)
            loss = log_loss(y_train,y_train_pred)
            child_fit.append(acc1)
            child_loss.append(loss)

        # next_state = best_child()
        next_fitness = max(child_fit)
        Loss = child_loss[child_fit.index(next_fitness)]
        # print("Loss:",loss)
        # Loss.append(l)
        # print(Loss)
        

        # If best child is an improvement,
        # move to that state and reset attempts counter
        if next_fitness > max(breeding_prob):
            population = next_gen
            breeding_prob = child_fit
            attempts = 0
        else:
            attempts += 1
    best_wts = population[breeding_prob.index(max(breeding_prob))]
    acc = max(breeding_prob)
    # print(Loss)
    return(best_wts,acc,Loss)

def levyAndGA(n):
    r = levy.rvs(size=n, scale=2)
    # print(r)
    losses = []
    max_acc=0
    for i in list(r):
        weights = np.random.uniform(-1, 1, 104)
        weights = weights*i
        mn = np.min(weights)
        mx = np.max(weights)
        weights1 = 6*((weights - mn)/(mx-mn)) - 3
        # print(weights1)
        nn.fit(X_train, y_train, weights1)
        y_train_pred = nn.predict(X_train)
        acc1 = accuracy_score(y_train, y_train_pred)
        # print(len(weights1))
        max_acc = 0
        best_wts = []
        if(acc1 != None and acc1 > 0.5):
            (best_fit, accuracy,Loss) = genetic_algorithm(weights1,max_iters=10)
            print(accuracy)
            losses.append(Loss)
            if(accuracy>max_acc):
                max_acc = accuracy
                best_wts = best_fit
    nn.fit(X_test, y_test, best_wts)
    y_test_pred = nn.predict(X_test)
    acc1 = accuracy_score(y_test, y_test_pred)
    print("Test accuracy obtained was: ",acc1)
    print(losses)

startTime = datetime.now()
levyAndGA(10)
print("\n\nExecution time is: ",datetime.now()-startTime)


def levyAndSA(n):
    nn1 = mlrose.NeuralNetwork(hidden_nodes=[4], activation='relu',
                               algorithm='simulated_annealing', max_iters=750,
                               bias=True, is_classifier=True, learning_rate=0.35,
                               early_stopping=False, clip_max=2, max_attempts=10,
                               random_state=3, curve=True)
    dummy_nn = NeuralNetwork(hidden_nodes=[4], activation='relu',
                            algorithm='dummy', max_iters=500,
                            bias=True, is_classifier=True, learning_rate=0.351,
                            early_stopping=False, clip_max=2, max_attempts=10,
                            random_state=3)
    r = levy.rvs(size=n, scale=2)
    max_acc = 0
    losses=np.array([])
    for i in list(r):
            weights = np.random.uniform(-1, 1, 104)
            weights = weights*i
            mn = np.min(weights)
            mx = np.max(weights)
            weights1 = 6*((weights - mn)/(mx-mn)) - 3
            dummy_nn.fit(X_train, y_train, weights1)
            y_train_pred = dummy_nn.predict(X_train)
            acc1 = accuracy_score(y_train, y_train_pred)
            if(acc1 != None and acc1 > 0.5):
                nn1.fit(X_train, y_train, weights1)
                y_train_pred = nn1.predict(X_train)
                acc2 = accuracy_score(y_train, y_train_pred)
                if acc2 != None and acc2 > max_acc:
                    max_acc = acc2
                    print(acc2)
                    losses=np.append(losses,nn1.fitness_curve)
                    losses= -losses
    x=np.arange(np.size(losses))
    plt.plot(x,losses)
    plt.ylabel("Loss")
    plt.xlabel("Iteration #")
    plt.title("Log_loss Plot")
    plt.show()

def eagle_strategy():
    '''Performs a levy flight as global search and either simulated annealing
       or genetic algorithm as a local search."
    '''
    alg=input("Enter local search algorithm\n1. Simulated_annealing\n2. Genetic_Algorithm: ")
    while alg.lower() not in ["simulated_annealing","genetic_algorithm"]:
        print("Oops, we haven't implemented that. Try Again")
        alg=input("Enter local search algorithm\n1. Simulated_annealing\n2. Genetic_Algorithm: ")
    n=int(input("Enter number of iterations of global search"))
    if(alg=="simulated_annealing"):
        pass
    if(alg=="genetic_algorithm"):
        pass        

levy_sim(5)
