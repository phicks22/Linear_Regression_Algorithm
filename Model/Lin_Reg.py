import numpy as np
import pandas as pd

class Linreg:

    def open_file(self, fileAsString):
        data = pd.read_csv(fileAsString)

        return data

    def error_mean(self, data):
        error_dict = dict()
        for row in col1 of dataframe:
            error_dict[col] = row - np.mean(data)

        return error_dict

    def error_mult(self, data):
        error_mult_dict = []




