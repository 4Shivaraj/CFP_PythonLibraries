'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to find the set difference of two arrays. The set difference
            will return the sorted, unique values in array1 that are not in array2.
            Expected Output:
            Array1: [ 0 10 20 40 60 80]
            Array2: [10, 30, 40, 50, 70, 90]
            Set difference between two arrays:
            [ 0 20 60 80]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_13)", file_name="data_log.log")


class NumericalPython:

    def find_difference(self, arr1, arr2):
        """
        Description:
             This function is used to find the set difference of two arrays.
        Parameter:
            arr1, arr2: The arr1 and arr2 to be checked
        Return:
            Returns None
        """
        try:
            lg.info(f'\nArray-1: {arr1} and \nArray-2: {arr2}')
            # differ_value = [element for element in arr1 if element not in arr2]
            differ_value = np.setdiff1d(arr1, arr2)
            lg.info(f'\ndifference of two arrays: {differ_value}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_array1 = [0, 10, 20, 40, 60, 80]
    my_array2 = [10, 30, 40, 50, 70, 90]
    np_obj = NumericalPython()
    np_obj.find_difference(my_array1, my_array2)
