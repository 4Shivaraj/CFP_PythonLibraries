'''
    @Author: Shivaraj
    @Date: 13-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 13-10-2022
    @Title: Write a Python program to get the powers of an array values element-wise.
            Note: First array elements raised to powers from second array
            Expected Output:
            Original array
            [0 1 2 3 4 5 6]
            First array elements raised to powers from second array, element-wise:
            [ 0 1 8 27 64 125 216]


'''
import sys

from data_log import get_logger

import numpy as np
import pandas as pd

lg = get_logger(name="(program_4)", file_name="data_log.log")


class PandasDataManipulation:

    def get_power_array(self, arr_data):
        """
        Description:
            This function is used to get the powers of an array values element-wise.
        Parameter:
            arr_data: The arr_data to be checked
        Return:
            Returns None
        """
        try:
            print(type(arr_data))
            lg.info(f"original array: {arr_data}")
            lg.info(
                f" First array elements raised to powers from second array, element-wise: {np.power(arr_data, 3)}")

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    arr_data = [0, 1, 2, 3, 4, 5, 6]
    pd_obj = PandasDataManipulation()
    pd_obj.get_power_array(arr_data)
