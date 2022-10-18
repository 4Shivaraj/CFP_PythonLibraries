'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: 15. Write a Python program compare two arrays using numpy.
            Array a: [1 2]
            Array b: [4 5]
            a > b
            [False False]
            a >= b
            [False False]
            a < b
            [ True True]
            a <= b
            [ True True]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_15)", file_name="data_log.log")


class NumericalPython:

    def compare_arrays(self, arr1, arr2):
        """
        Description:
             This function is used to compare two arrays.
        Parameter:
            arr1, arr2: The arr1 and arr2 to be checked
        Return:
            Returns None
        """
        try:
            array1 = np.array(arr1)
            array2 = np.array(arr2)
            lg.info(f'Array 1: {arr1}')
            lg.info(f'Array 2: {arr2}')
            lg.info('Array 1 > Array 2')
            lg.info(np.greater(array1, array2))
            lg.info('Array 1 >= Array 2')
            lg.info(np.greater_equal(array1, array2))
            lg.info('Array 1 < Array 2')
            lg.info(np.less(array1, array2))
            lg.info('Array 1 <= Array 2')
            lg.info(np.less_equal(array1, array2))
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_array1 = [0, 10]
    my_array2 = [40, 50]
    np_obj = NumericalPython()
    np_obj.compare_arrays(my_array1, my_array2)
