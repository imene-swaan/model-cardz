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
    subtitle = ''
    description = ''
    model_name = 'Unkown model'

    def __init__(
        self,
        x_train:pd.DataFrame= pd.DataFrame(),
        y_train:pd.Series=pd.Series(),
        x_test:pd.DataFrame=pd.DataFrame(),
        y_test:pd.Series=pd.Series(),
        y_pred:pd.Series=pd.Series(),

        model_name:str=model_name,
        title:str=title,
        subtitle:str=subtitle,
        description:str= description
    ):
        
        self.xtrain = x_train
        self.ytrain = y_train
        self.xtest = x_test
        self.ytest = y_test
        self.ypred = y_pred
        
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.model_name = model_name
    

        

