'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a python program to display NumPy array elements of floating values with given precision.
            Original array elements:
            [ 0.26153123 0.52760141 0.5718299 0.5927067 0.7831874 0.69746349
            0.35399976 0.99469633 0.0694458 0.54711478]
            Print array values with precision 3:
            [ 0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_24)", file_name="data_log.log")


class NumericalPython:

    def display_with_precision(self):
        """
        Description:
             This function is used to display NumPy array elements of floating values with given precision
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array = np.random.rand(10)
            lg.info(f"original array elements: \n{my_array}")
            np.set_printoptions(precision=3)
            lg.info(f"array values with precision 3: \n{my_array}")

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.display_with_precision()
