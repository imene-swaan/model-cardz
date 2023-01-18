


class Cardz():
    """
    This class creates meta data for the model card generated
    ----------
    title: str,
    subtitle: str,
    description: str,
    
    x_train: array
    """

    import numpy as np

    def __init__(
        self,
        title:str,
        subtitle:str,
        description:str,
        xtrain
    ):
        if type(x_train) is not np.ndarray:
            self.x_train = np.asarray(xtrain)

        else:
            self.x_train = xtrain
    

        

