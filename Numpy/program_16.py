'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to create a contiguous flattened array.
            Original array:
            [[10 20 30]
            [20 40 50]]
            New flattened array:
            [10 20 30 20 40 50]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_16)", file_name="data_log.log")


class NumericalPython:

    def flattened_array(self, arr1):
        """
        Description:
             This function is used to create a contiguous flattened array.
        Parameter:
            arr1: The arr1 to be checked
        Return:
            Returns None
        """
        try:
            array1 = np.array(arr1)
            lg.info(f'Array-1: \n{array1}')
            flattened_array = np.ravel(array1)
            lg.info(f'\ncontiguous flattened array: {flattened_array}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_array = [[10, 20, 30], [20, 40, 50]]
    np_obj = NumericalPython()
    np_obj.flattened_array(my_array)
