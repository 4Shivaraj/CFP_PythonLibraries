'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to suppresses the use of scientific notation for small
            numbers in numpy array.
            Expected Output:
            Original array elements:
            [ 1.60000000e-10 1.60000000e+00 1.20000000e+03 2.35000000e-01]
            Print array values with precision 3:
            [ 0. 1.6 1200. 0.235]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_25)", file_name="data_log.log")


class NumericalPython:

    def suppresses_small_num(self, arr):
        """
        Description:
            This function is used to suppresses the use of scientific notation for small
            numbers in numpy array
        Parameter:
            arr: The arr to be checked 
        Return:
            Returns None
        """
        try:
            my_array1 = np.array(arr)
            lg.info(f"original array elements: \n{my_array1}")
            np.set_printoptions(suppress=True)
            lg.info(
                f"array values with suppresses for small numbers: \n{my_array1}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_arr = [2.6e-10, -.56, 1.6, 1200, .235]
    np_obj = NumericalPython()
    np_obj.suppresses_small_num(my_arr)
