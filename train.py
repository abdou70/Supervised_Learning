import numpy as np
from cost import compute_cost

#This function allow to add a bias in the dataset it means a colum of 1 for developping the future linear model
#f(x)=ax+b
def add_ones(X):
    ###### fill the code ####

  X_new = np.hstack([np.ones((X.shape[0],1)),X])
    #########################


  return X_new

#This ones is the train function
def Train(X, y, lr, epoch):
    m = len(y)
    X = add_ones(X.values)
    #Initialise the weight for performing the prediction of the modfel
    theta = np.zeros(X.shape[1])
    #Initialise an array to save the evolution of this model
    cost_history= np.zeros(epoch)

    ######## fill the code #######

    for i in range(epoch):
        cost_history [i]= compute_cost(X,y,theta) 
        theta_new = theta - (1/m)*lr * X.T .dot(X.dot(theta)-y) 
        theta = theta_new
    ##############################

    return  theta, cost_history