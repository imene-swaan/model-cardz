import pandas as pd
from typing import Literal, Optional
from jinja2 import Environment, FileSystemLoader
import jinja2
import os

from utils import utils

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
        model,

        x_train:pd.DataFrame= pd.DataFrame(),
        y_train:pd.Series=pd.Series(),
        x_test:pd.DataFrame=pd.DataFrame(),
        y_test:pd.Series=pd.Series(),
        y_pred:pd.Series=pd.Series(),

        title:str = 'auto',
        intended_use: str= 'auto',
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
        
        
        self.intended_use = intended_use

        self.model_name, self.task = utils.get_task(self.model)

        if self.title == 'auto':
            self.title = 'The ' + self.model_name + ' Model Card'
        else:
            self.title = title 
        
        if self.intended_use == 'auto':
            self.intended_use = 'This experiment was conducted to test the performance of the ' + self.model_name + ' ' + self.task + 'model on our dataset.'
        else:
            self.intended_use = intended_use


        self.subtitle = 'This model card was generated using the Cardz library.'
        

        self.model_description = utils.gpt3_model_description(self.model_name, self.task)













        








    
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, Y = load_iris(return_X_y=True)
x, tx, y, ty = train_test_split(X, Y, test_size=0.33, random_state=42)

clf = LogisticRegression(max_iter=200).fit(x, y)
yp = clf.predict(tx)
        

def main():

    card = Cardz(model = 'regression', x_train= x, y_train= y, x_test= tx, y_test= ty, y_pred= yp)
    card.get_card('cardz_3.md')

    print(card.model)
    


if __name__ == "__main__":
    main()
