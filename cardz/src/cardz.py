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

        x_train:pd.DataFrame,
        y_train:pd.Series,
        x_test:pd.DataFrame,
        y_test:pd.Series,
        y_pred:pd.Series,

        #task: Literal['classification', 'regression', 'clustering'] = 'classification',

        title:str = 'auto',
        intended_use: str= 'auto',
    ):
        
        self.model = model

        self.xtrain = x_train
        self.ytrain = y_train
        self.xtest = x_test
        self.ytest = y_test
        self.ypred = y_pred
        
        self.title = title
        self.intended_use = intended_use

        self.model_name, self.task = utils.get_task(self.model)

        

        if self.title == 'auto':
            self.title = 'The ' + self.model_name + ' Card'
        else:
            self.title = title 
        


        self.subtitle = 'This model card was generated using the Cardz library.'
        

        self.model_description = utils.gpt3_model_description(self.model_name, self.task)

        self.model_type = utils.get_model_type(self.model_description)

        if self.intended_use == 'auto':
            self.intended_use = f'This experiment was conducted to test the performance of the {self.model_type} {self.task} model: {self.model_name} on our dataset.'
        else:
            self.intended_use = intended_use


        self.model_params = utils.get_model_params(self.model)

        self.model_params_description = utils.gpt3_model_params_description(self.model_name)



    
    
    def metrics(self):
        meta_data = {
            'title': self.title,
            'subtitle': self.subtitle,
            'model_name': self.model_name,
            'model_type': self.model_type,
            'model_description': self.model_description,
            'model_params': self.model_params,
            'model_params_description': self.model_params_description,
            'intended_use': self.intended_use,
            'task': self.task
        }
        return meta_data
    


    def get_card(self, file_name: str= 'model_card', save_metrics: bool= True):
        """
        This function generates a model card from the meta data.
        """
        meta_data = self.metrics()

        # --- General outputs directory
        if not os.path.exists('../outputs/cardz'):
            os.mkdir('../outputs/cardz')

        # --- Model card directory
        if not os.path.exists(f'../outputs/cardz/{self.model_name}'):
            os.mkdir(f'../outputs/cardz/{self.model_name}')



        # --- Save the meta data
        if save_metrics:
            utils.save_meta_data(meta_data, f'../outputs/cardz/{self.model_name}/metrics.json')



        # --- Fill the template
        content = utils.fill_template(self.model_type, self.task, meta_data)

        # --- Save the model card
        with open(f'../outputs/cardz/{self.model_name}/{file_name}.md', 'w') as f:
            f.write(content)

        
        print(f'card saved in directory: ../outputs/cardz/{self.model_name}/{file_name}.md')

      
    












        








    
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, Y = load_iris(return_X_y=True)
x, tx, y, ty = train_test_split(X, Y, test_size=0.33, random_state=42)

clf = LogisticRegression(max_iter=200).fit(x, y)
yp = clf.predict(tx)
        

def main():

    card = Cardz(model = clf, x_train= x, y_train= y, x_test= tx, y_test= ty, y_pred= yp)
    card.get_card()
    


if __name__ == "__main__":
    main()
