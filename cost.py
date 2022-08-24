import numpy as np

#cost function
def compute_cost(X, y, theta):
    ######## fill the code ###########

  loss= (1/2)* np.sum((X.dot(theta)-y)**2)
    ##################################

  return loss
