'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to add a border (filled with 0's) around an existing array.
            Expected Output:
            Original array:
            [[ 1. 1. 1.]
            [ 1. 1. 1.]
            [ 1. 1. 1.]]
            1 on the border and 0 inside in the array
            [[ 0. 0. 0. 0. 0.]
            [ 0. 1. 1. 1. 0.]
            [ 0. 1. 1. 1. 0.]
            [ 0. 1. 1. 1. 0.]
            [ 0. 0. 0. 0. 0.]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_6)", file_name="data_log.log")


class NumericalPython:

    def add_border(self):
        """
        Description:
             This function is used to create a border (filled with 0's) around an existing array.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array = np.ones((3, 3))
            lg.info(f"original array: \n{my_array}")
            updated_array = np.pad(my_array, pad_width=1,
                                   mode='constant', constant_values=0)
            lg.info(f"after filling '0' inside array: \n{updated_array}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.add_border()
