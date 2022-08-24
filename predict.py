import numpy as np

from train import add_ones

#predict function
def predict(X, theta):
  ########## fill the code #########

  X=add_ones(X.values)
  yPred= np.dot(X,theta)


  #################################

  return yPred

