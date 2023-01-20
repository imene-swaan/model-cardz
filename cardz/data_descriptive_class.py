from cardz_class import Cardz
import pandas as pd

class Descriptive_statistics(Cardz):
    """
    This class creates descriptive statistics meta data for the model card generated
    ----------
    
    x_train: pandas dataframe
    y_train: pandas series
    x_test: pandas dataframe
    y_test: pandas series
    y_pred: pandas series

    """

    def __init__(self, Data_stat:bool= True):
        self.Data_stat = Data_stat
        super().__init__(self)
    
    
    def Training_data_description(self):
        self.X_description = self.xtrain.describe().to_dict()
        self.y_description = self.ytrain.describe().to_dict()

