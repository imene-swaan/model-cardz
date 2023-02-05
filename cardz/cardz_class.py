import pandas as pd
from typing import Literal


class Cardz():
    """
    This class creates meta data for the model card generated
    ----------
    title: str,
    subtitle: str,
    description: str,
    
    x_train: array
    """


    def __init__(
        self,
        model: Literal["auto", "regression", "classification"],

        x_train:pd.DataFrame= pd.DataFrame(),
        y_train:pd.Series=pd.Series(),
        x_test:pd.DataFrame=pd.DataFrame(),
        y_test:pd.Series=pd.Series(),
        y_pred:pd.Series=pd.Series(),

        title:str= 'My Model Card',
        subtitle:str= '',
        description:str= ''
    ):
        


        if model == 'auto':
            self.model = 'Unkown model'
        else:
            self.model = model

        self.xtrain = x_train
        self.ytrain = y_train
        self.xtest = x_test
        self.ytest = y_test
        self.ypred = y_pred
        
        self.title = title
        self.subtitle = subtitle
        self.description = description

    

        

