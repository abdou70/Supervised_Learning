import numpy as np

#This function is defined to split the data
def split_data(df, train_percent):
  ########## fill the code ########
    np.random.seed(1)
    perm=np.random.permutation(df.index)

    n=len(df)

    train_index = int(train_percent * n)

    train = df.iloc[perm[:train_index]]
    test = df.iloc[perm[train_index:]]


    X_train = train.iloc[:,:-1]
    Y_train = train.iloc[:,-1]

    X_test= test.iloc[: , :-1]
    Y_test = test.iloc[:,-1]
    return X_train, X_test, Y_train, Y_test