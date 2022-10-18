'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to create an array which looks like below array.
            Expected Output:
            [[ 0. 0. 0.]
            [ 1. 0. 0.]
            [ 1. 1. 0.]
            [ 1. 1. 1.]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_19)", file_name="data_log.log")


class NumericalPython:

    def create_array(self):
        """
        Description:
             This function is used to create an array using tri() function
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array = np.tri(4, 3, -1)
            # The tri() function is used to get an array with ones at and below the given diagonal and zeros elsewhere.
            lg.info(f'final array: \n{my_array}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.create_array()
