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


l = []


def generateColumns(start, end):
    for i in range(start, end+1):
        l.extend([str(i)+'X', str(i)+'Y'])
    return l


eyes = generateColumns(1, 12)

# reading in the csv as a dataframe
df = pd.read_csv(
    "/Users/pragnya/Documents/GitHub/Metaheuristic-NN/Eyes.csv")

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
nn1 = mlrose.NeuralNetwork(hidden_nodes=[4], activation='relu',
                           algorithm='simulated_annealing', max_iters=400,
                           bias=True, is_classifier=True, learning_rate=0.1,
                           early_stopping=False, clip_max=2, max_attempts=10,
                           random_state=3,curve=True)

nn = NeuralNetwork(hidden_nodes=[4], activation='relu',
                   algorithm='hi', max_iters=500,
                   bias=True, is_classifier=True, learning_rate=0.351,
                   early_stopping=False, clip_max=2, max_attempts=10,
                   random_state=3)

# printing execution time of script


def levy_walk(n):
    r = levy.rvs(size=n, scale=2)
    # print(r)
    max_acc=0
    max_wts = []
    for i in list(r):
        weights = np.random.uniform(-1, 1, 104)
        weights = weights*i
        mn = np.min(weights)
        mx = np.max(weights)
        weights1 = 6*((weights - mn)/(mx-mn)) - 3
        nn.fit(X_train, y_train, weights1)
        y_train_pred = nn.predict(X_train)
        acc1 = accuracy_score(y_train, y_train_pred)
        if(acc1 != None and acc1 > 0.6):
            nn1.fit(X_train, y_train, weights1)
            y_train_pred = nn1.predict(X_train)
            acc2 = accuracy_score(y_train, y_train_pred)
            print(acc2)
            if acc2>max_acc:
                max_acc=acc2
                max_wts = weights1
                #print(nn1.fitness_curve)
    print("Best accuracy obtained: ",max_acc)

startTime = datetime.now()
levy_walk(50)
print("Execution time in seconds = ", datetime.now() - startTime)
print("\n")
#print("Execution time in seconds = ", datetime.now() - startTime)
