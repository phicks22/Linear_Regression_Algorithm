import numpy as np
import csv

class Linreg:

    def __init__(self, file):
        self.file = file
        self.error_dict = dict()
        self.err_mult_dict = dict()
        self.slope = 0
        self.y_int = 0


    def open_file(self, fileAsString):
        dict_list = list()
        with open(fileAsString) as f:
            records = csv.DictReader(f)
            for row in records:
                dict_list.append(row)

        return dict_list

    def error_mean(self, data):
        error_dict = dict()
        for row in col1 of dataframe:
            error_dict[col] = row - np.mean(data)

        return error_dict

    def error_mult(self, data):
        error_mult_dict = dict()
        for row in col1 of dataframe:
            error_mult_dict = row - np.mean(data)

        return error_mult_dict

    def line_equation(self, error_mult_dict, error_dict):
        sum_squares = 0
        for i in error_mult_dict[0]:
            sum_squares += i

        x_mean_diff = 0
        for i in error_dict[0]:
            x_mean_diff += i

        self.slope = sum_squares / x_mean_diff

        return self.slope

    def y_int(self):
        intercept = 




