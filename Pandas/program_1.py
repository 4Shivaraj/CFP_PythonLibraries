'''
    @Author: Shivaraj
    @Date: 13-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: Write a Python program to create and display a one-dimensional array-like object
            containing an array of data using Pandas module.
'''

import sys

from data_log import get_logger

import pandas as pd

lg = get_logger(name="(program_1)", file_name="data_log.log")


class PandasDataManipulation:

    def display_1D_array(self, arr_data):
        """
        Description:
             This function is used to display a one-dimensional array-like object
        Parameter:
            arr_data: The arr_data to be checked
        Return:
            Returns None
        """
        try:
            my_series = pd.Series(arr_data)
            lg.info(f" one-dimensional array: \n{my_series}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    arr_data = [2, 4, 6, 8, 10]
    pd_obj = PandasDataManipulation()
    pd_obj.display_1D_array(arr_data)
