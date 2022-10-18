'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to find common values between two arrays.
            Expected Output:
            Array1: [ 0 10 20 40 60]
            Array2: [10, 30, 40]
            Common values between two arrays:
            [10 40]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_12)", file_name="data_log.log")


class NumericalPython:

    def find_common_values(self, arr1, arr2):
        """
        Description:
             This function is used to find common values between two arrays
        Parameter:
            arr1, arr2: The arr1 and arr2 to be checked
        Return:
            Returns None
        """
        try:
            lg.info(f'\nArray-1: {arr1} and \nArray-2: {arr2}')
            # common_values = [element for element in arr1 if element in arr2]
            common_values = np.intersect1d(arr1, arr2)
            lg.info(f'\ncommon_values: {common_values}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_array1 = [0, 10, 20, 40, 60]
    my_array2 = [10, 30, 40]
    np_obj = NumericalPython()
    np_obj.find_common_values(my_array1, my_array2)
