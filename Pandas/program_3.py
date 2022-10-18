'''
    @Author: Shivaraj
    @Date: 13-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: Write a Python program to add, subtract, multiple and divide two Pandas Series.
            Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
'''

import sys

from data_log import get_logger

import pandas as pd

lg = get_logger(name="(program_3)", file_name="data_log.log")


class PandasDataManipulation:

    def calculator(self, arr_data1, arr_data2):
        """
        Description:
             This function is used to add, subtract, multiple and divide two Pandas Series.
        Parameter:
            arr_data1 and arr_data2: The arr_data1 and arr_data2 to be checked
        Return:
            Returns None
        """
        try:
            my_series1 = pd.Series(arr_data1)
            my_series2 = pd.Series(arr_data2)
            add_series = my_series1 + my_series2
            lg.info(f" adding two series: \n{add_series}")
            substract_series = my_series1 - my_series2
            lg.info(f" substract two series: \n{substract_series}")
            multiply_series = my_series1 * my_series2
            lg.info(f" multiply two series: \n{multiply_series}")
            divide_series = my_series1 / my_series2
            lg.info(f" divide two series: \n{divide_series}")

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    arr_data1 = [2, 4, 6, 8, 10]
    arr_data2 = [1, 3, 5, 7, 9]
    pd_obj = PandasDataManipulation()
    pd_obj.calculator(arr_data1, arr_data2)
