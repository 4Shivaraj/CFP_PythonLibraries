'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to create a 2d array with 1 on the border and 0 inside.
            Expected Output:
            Original array:
            [[ 1. 1. 1. 1. 1.]
            [ 1. 1. 1. 1. 1.]
            [ 1. 1. 1. 1. 1.]
            [ 1. 1. 1. 1. 1.]
            [ 1. 1. 1. 1. 1.]]

            1 on the border and 0 inside in the array
            [[ 1. 1. 1. 1. 1.]
            [ 1. 0. 0. 0. 1.]
            [ 1. 0. 0. 0. 1.]
            [ 1. 0. 0. 0. 1.]
            [ 1. 1. 1. 1. 1.]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_5)", file_name="data_log.log")


class NumericalPython:

    def create_2d_array(self):
        """
        Description:
             This function is used to create a 2d array with 1 on the border and 0 inside.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array = np.ones((5, 5))
            lg.info(f"original array: \n{my_array}")
            my_array[1:4, 1:4] = 0
            lg.info(f"array after updating: \n{my_array}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.create_2d_array()
