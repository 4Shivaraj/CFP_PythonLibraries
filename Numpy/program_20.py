'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to concatenate two 2-dimensional arrays.
            Expected Output:
            Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
            Expected Output:
            [[ 0 1 3 0 2 4]
            [ 5 7 9 6 8 10]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_20)", file_name="data_log.log")


class NumericalPython:

    def concat_2d_array(self, arr1, arr2):
        """
        Description:
             This function is used to concatenate two 2-dimensional arrays.
        Parameter:
            arr1, arr2: The arr1 and arr2 to be checked
        Return:
            Returns None
        """
        try:
            my_array1 = np.array(arr1)
            my_array2 = np.array(arr2)
            result_array = np.concatenate((my_array1, my_array2), axis=1)
            lg.info(f'final array: \n{result_array}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    array_1 = [[0, 1, 3], [5, 7, 9]]
    array_2 = [[0, 2, 4], [6, 8, 10]]
    np_obj = NumericalPython()
    np_obj.concat_2d_array(array_1, array_2)
