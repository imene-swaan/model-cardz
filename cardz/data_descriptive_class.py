from cardz_class import Cardz
import pandas as pd
import numpy as np

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

    def __init__(self, x_train, y_train, model, Data_stat:bool= True):
        super().__init__(x_train, y_train, model)
        self.Data_stat = Data_stat

        if self.Data_stat:
            self.xresults = {}

        if self.model == 'auto':
            self.state = 'shut'
        
    
    
    def X_description(self):
        self.xresults['x_train_0'] = self.xtrain.shape[0]
        self.xresults['x_train_1'] = self.xtrain.shape[1]

        a = self.xtrain.dtypes.to_list()

        from collections import Counter
        t = Counter(a).keys()
        c = Counter(a).values()

        self.xresults['number_x_types'] = len(t)
        self.xresults['x_types'] = [[t[i], c[i]] for i in range(len(t))]
    
        return self.xresults
    

    def Y_description(self):
        self.type_y_train = self.ytrain.dtype
        if self.type_y_train != object:
            self.mean_y_train = np.mean(self.ytrain)
            self.std_y_train = np.std(self.ytrain)

            return self.type_y_train, self.mean_y_train, self.std_y_train

        else:
            from collections import Counter

            t = Counter(self.ytrain.to_list()).keys()
            c = Counter(self.ytrain.to_list()).values()

            self.number_classes = len(t)
            self.class_counts = [[t[i], c[i]] for i in range(len(t))]

            return self.type_y_train, self.number_classes, self.class_counts
