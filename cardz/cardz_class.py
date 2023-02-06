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


    def get_meta_data(self):
        meta_data = {"title": self.title ,"subtitle": self.subtitle, 'description': self.description, 'model': self.model}
    
        return meta_data



    def fill_template(self, template, meta_data:dict):
        from jinja2 import Environment, FileSystemLoader

        environment = Environment(loader=FileSystemLoader("Templates/"))

        temp = environment.get_template(template)
        content = temp.render(meta_data)

        return content


    def get_card(self, file_name: str):

        meta_data = self.get_meta_data()
        content = self.fill_template('markdown.md', meta_data)
        
        with open('results/' + file_name, mode = 'w', encoding= 'utf-8') as message:
            message.write(content)


        
        print('card saved in directory: ../results/cardz_2.md')
    








    
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, Y = load_iris(return_X_y=True)
x, tx, y, ty = train_test_split(X, Y, test_size=0.33, random_state=42)

clf = LogisticRegression(random_state=0).fit(x, y)
yp = clf.predict(tx)
        

def main():

    card = Cardz(model = 'classification', x_train= x, y_train= y, x_test= tx, y_test= ty, y_pred= yp)
    return card.get_card('cardz_3.md')
    


if __name__ == "__main__":
    main()