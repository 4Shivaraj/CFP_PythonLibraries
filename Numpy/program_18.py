'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to create a 3-D array with ones on a diagonal and zeros
            elsewhere.
            Expected Output:
            [[ 1. 0. 0.]
            [ 0. 1. 0.]
            [ 0. 0. 1.]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_18)", file_name="data_log.log")


class NumericalPython:

    def identity_matrix(self):
        """
        Description:
             This function is used to create a 3-D array with ones on a diagonal and zeros
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            array_3d = np.eye(3)
            lg.info(f'identity matrix: \n{array_3d}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.identity_matrix()
