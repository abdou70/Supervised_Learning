
from train import Train
from data import X_train,X_test,Y_train,Y_test
import numpy as np
import matplotlib.pyplot as plt

#Training the model with the hyperparameter
epoch = 30
learning_rate=0.3
theta, loss_history = Train(X_train, Y_train, learning_rate, epoch)

#This is the main file
#Finally you can how our loss decrease 
plt.figure()
plt.plot(np.arange(epoch), loss_history, c='blue')
plt.xlabel('Iterations')
plt.ylabel('Cost, ' + r'$J(\theta)$')
plt.show()