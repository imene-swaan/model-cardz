from .cardz_class import Cardz
import pandas as pd

class _descriptive_stat(Cardz):
    """
    This class creates descriptive statistics meta data for the model card generated
    ----------
    
    x_train: pandas dataframe
    y_train: pandas series
    x_test: pandas dataframe
    y_test: pandas series
    y_pred: pandas series

    """

    def __init__(
        self,
        x_train:pd.Dataframe=None,
        y_train:pd.Series=None,
        x_test:pd.Dataframe=None,
        y_test:pd.Series=None,
        y_pred:pd.Series=None
    ):

    
        self.xtrain = x_train
        self.ytrain = y_train
        self.xtest = x_test
        self.ytest = y_test
        self.ypred = y_pred
        Cardz.__init__(self, self.xtrain , self.ytrain, self.xtest, self.ytest, self.ypred)