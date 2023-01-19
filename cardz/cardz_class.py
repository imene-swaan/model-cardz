import pandas as pd


class Cardz():
    """
    This class creates meta data for the model card generated
    ----------
    title: str,
    subtitle: str,
    description: str,
    
    x_train: array
    """
    title = 'My Model Card'
    subtitle = ' '
    description = ' '
    model_name = 'Regression'

    def __init__(
        self,
        x_train:pd.Dataframe=None,
        y_train:pd.Series=None,
        x_test:pd.Dataframe=None,
        y_test:pd.Series=None,
        y_pred:pd.Series=None,

        model_name:str=model_name,
        title:str=title,
        subtitle:str=subtitle,
        description:str= description
    ):
        
        import numpy as np

        
        self.xtrain = x_train
        self.ytrain = y_train
        self.xtest = x_test
        self.ytest = y_test
        self.ypred = y_pred
        
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.model_name = model_name
    

        

