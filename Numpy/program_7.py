'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
            Checkerboard pattern:
            [[0 1 0 1 0 1 0 1]
            [1 0 1 0 1 0 1 0]
            [0 1 0 1 0 1 0 1]
            [1 0 1 0 1 0 1 0]
            [0 1 0 1 0 1 0 1]
            [1 0 1 0 1 0 1 0]
            [0 1 0 1 0 1 0 1]
            [1 0 1 0 1 0 1 0]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_7)", file_name="data_log.log")


class NumericalPython:

    def check_board_pattern(self):
        """
        Description:
             This function is used to create a checkerboard pattern.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array = np.ones((8, 8))
            lg.info(f"original array: \n{my_array}")
            my_array[::2, ::2] = 0
            my_array[1::2, 1::2] = 0
            lg.info(f"checkerboard pattern: \n{my_array}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.check_board_pattern()
