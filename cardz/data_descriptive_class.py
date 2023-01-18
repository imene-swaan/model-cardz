from typing import List

class _descriptive_stat():
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
        xtrain,
        y_train,
        x_test,
        y_test
    ):

    
    @staticmethod
    def _mean(X) -> list:
        
        