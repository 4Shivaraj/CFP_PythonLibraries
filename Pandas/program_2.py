'''
    @Author: Shivaraj
    @Date: 13-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: Write a Python program to convert a Panda module Series to Python list and it's type.
'''
import sys

from data_log import get_logger

import pandas as pd

lg = get_logger(name="(program_2)", file_name="data_log.log")


class PandasDataManipulation:

    def convert_series_to_list(self, arr_data):
        """
        Description:
             This function is used to convert a Panda module Series to Python list and it's type.
        Parameter:
            arr_data: The arr_data to be checked
        Return:
            Returns None
        """
        try:
            my_series = pd.Series(arr_data)
            lg.info(
                f" pandas series: \n{my_series} and \ntype: {type(my_series)}")
            lg.info(f"Convert pandas series to python list: ")
            lg.info(
                f" \npython list: {my_series.to_list()} and \ntype: {type(my_series.to_list())}")

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    arr_data = [2, 4, 6, 8, 10]
    pd_obj = PandasDataManipulation()
    pd_obj.convert_series_to_list(arr_data)
