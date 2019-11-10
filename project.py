# Author : Ameya Bhamare
import mlrose
from datetime import datetime
startTime = datetime.now()

l = []
def generateColumns(start, end):
    for i in range(start, end+1):
        l.extend([str(i)+'X', str(i)+'Y'])
    return l

eyes = generateColumns(1, 12)

# reading in the csv as a dataframe
import pandas as pd
df = pd.read_csv('EYES.csv')

# selecting the features and target
X = df[eyes]
y = df['truth_value']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 42)

# Data Normalization
from sklearn.preprocessing import StandardScaler as SC
sc = SC()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

import numpy as np
X_train, y_train, X_test, y_test = np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test)

#print(df_results)
nn= mlrose.NeuralNetwork(hidden_nodes = [4], activation = 'relu', \
                                 algorithm = 'random_hill_climb', max_iters = 200, \
                                 bias = True, is_classifier = True, learning_rate = 0.351, \
                                 early_stopping = False, clip_max = 2, max_attempts =100, \
                                 random_state = 3)
nn.fit(X_train,y_train)
from sklearn.metrics import accuracy_score
y_train_pred = nn.predict(X_train)
y_test_pred = nn.predict(X_test)
acc1=accuracy_score(y_train,y_train_pred)
acc2=accuracy_score(y_test,y_test_pred)
print(acc1)
print(acc2)
# printing execution time of script
print("\n")
print("Execution time in seconds = ", datetime.now() - startTime)
